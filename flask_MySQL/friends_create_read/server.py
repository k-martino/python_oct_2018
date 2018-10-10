from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "Shhhhhhhh"


@app.route("/")
def index():
    mysql = connectToMySQL("friendsDB")
    query = mysql.query_db("SELECT * FROM friends;")
    return render_template("index.html", friends=query)


@app.route("/insert", methods=['POST'])
def insert():
    mysql = connectToMySQL("friendsDB")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    id = mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
