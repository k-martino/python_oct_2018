from flask import Flask
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL("friendsDB")
print("all the users", mysql.query_db("SELECT * FROM Users;"))
if __name__ == "__main__":
    app.run(debug=True)