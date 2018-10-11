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

    # Validate first name
    if len(request.form["first_name"]) < 1:
        flash("First name cannot be blank!", category="first_name")
    elif not NAME_REGEX.match(request.form["first_name"]):
        flash("Name cannot contain special characters!", category="first_name")
    else:
        session["first_name"] = request.form["first_name"]

    # Validate last name
    if len(request.form["last_name"]) < 1:
        flash("Last name cannot be blank!", category="last_name")
    elif not NAME_REGEX.match(request.form["last_name"]):
        flash("Name cannot contain special characters!", category="last_name")

    # Validate email
    mysql = connectToMySQL("login_registration")
    emailquery = "SELECT * FROM users WHERE email = %(email)s;"
    emaildata = {"email": request.form["email"]}
    emailcheck = mysql.query_db(emailquery, emaildata)
    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!", category="email")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address!", category="email")
    elif emailcheck:
        flash("Email already in use!", category="email")

    # Validate password
    if len(request.form["password"]) < 7:
        flash("Password must be at least 8 characters!", category="password")
    elif request.form["password"] != request.form["confirmpassword"]:
        flash("Passwords must match!", category="confirmpassword")

    if "_flashes" in session.keys():
        return redirect("/")
    else:  # Encrypt password
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
        session["first_name"] = result[0]["first_name"]
        return redirect("/wall")


@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL("login_registration")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email": request.form["email"]}
    result = mysql.query_db(query, data)
    if result:  # is username in database?
        if bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
            session["userid"] = result[0]["id"]
            session["first_name"] = result[0]["first_name"]
            return redirect("/wall")
    flash("You could not be logged in", category="login_status")
    return redirect("/")


@app.route("/wall")
def success():
    if "userid" not in session:
        return redirect("/")
    else:
        # Get all messages from database
        mysql = connectToMySQL("login_registration")
        query = "SELECT * FROM messages WHERE recipient_id = %(userid)d;"
        data = {"userid": session["userid"]}
        receivedmsgs = mysql.query_db(query, data)

        # Get all friend ids from database
        mysql = connectToMySQL("login_registration")
        query = "SELECT * FROM users WHERE id != %(userid)d;"
        friends = mysql.query_db(query, data)

    return render_template("wall.html", session=session, receivedmsgs=receivedmsgs, friends=friends)


@app.route("/message/<int:recipient_id>", methods=["POST"])
def msgsend(recipient_id):
    mysql = connectToMySQL("login_registration")
    query = "INSERT INTO messages (message, sender_id, recipient_id) VALUES (%(message)s, %(sender_id)d, %(recipient_id)d);"
    data = {
        "message": request.form["message"],
        "sender_id": session["id"],
        "recipient_id": recipient_id,
    }
    mysql.query_db(query, data)
    return redirect("/wall")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
