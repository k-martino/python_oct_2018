from flask import Flask, flash, redirect, render_template, request, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
NAME_REGEX = re.compile(r"^[a-zA-Z- ]+$")

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Shhhhhhhh"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/createUser", methods=["POST"])
def create():
    mysql = connectToMySQL("login_registration")
    emailquery = "SELECT * FROM users WHERE email = %(email)s;"
    emaildata = {"email": request.form["email"]}
    emailcheck = mysql.query_db(emailquery, emaildata)

    if len(request.form["first_name"]) < 1:
        flash("First name cannot be blank!", category="first_name")
    elif not NAME_REGEX.match(request.form["first_name"]):
        flash("Name cannot contain special characters!", category="first_name")

    if len(request.form["last_name"]) < 1:
        flash("Last name cannot be blank!", category="last_name")
    elif not NAME_REGEX.match(request.form["last_name"]):
        flash("Name cannot contain special characters!", category="last_name")

    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!", category="email")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address!", category="email")
    elif emailcheck:
        flash("Email already in use!", category="email")

    if len(request.form["password"]) < 7:
        flash("Password must be at least 8 characters!", category="password")
    elif request.form["password"] != request.form["confirmpassword"]:
        flash("Passwords must match!", category="confirmpassword")

    if "_flashes" in session.keys():
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        mysql = connectToMySQL("login_registration")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password_hash": pw_hash,
        }
        mysql.query_db(query, data)

        mysql = connectToMySQL("login_registration")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email": request.form["email"]}
        result = mysql.query_db(query, data)

        session["userid"] = result[0]["id"]
        session["name"] = result[0]["first_name"]
        return redirect("/success")


@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL("login_registration")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email": request.form["email"]}
    result = mysql.query_db(query, data)
    if result:  # is username in database?
        if bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
            session["userid"] = result[0]["id"]
            session["name"] = result[0]["first_name"]
            return redirect("/success")
    flash("You could not be logged in")
    return redirect("/")


@app.route("/success")
def success():
    if "userid" not in session:
        return redirect("/")
    return render_template("success.html", session=session)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
