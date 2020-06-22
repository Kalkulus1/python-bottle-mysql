#imports
from bottle import Bottle, request, run, response, static_file, redirect, template
import mysql.connector
import json

app = Bottle()

#Mysql Connection
conn = mysql.connector.connect(
  host="localhost",
  user="kalkulus",
  password="kalkulus1234",
  database="test"
)
cursor = conn.cursor()
print(conn)

#Index page redirect to login.
@app.route("/")
def index():
    return redirect("/login")

#Register page
@app.route("/register")
def register():
    return static_file("register.html", root="views/")

@app.route("/register", method="POST")
def do_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')

    if password == password2:
        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (username, password)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "record inserted.")
        return redirect("/dashboard")
    else:
        return "<p>Registeration failed!</p>"

@app.route("/dashboard")
def dashboard():
    return static_file("home.html",root="views/")

#Login page
@app.route("/login")
def login():
    return static_file("login.html", root="views/")

@app.route("/login", method="POST")
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    sql = "SELECT * FROM user WHERE username = %s and password = %s"
    val = (username, password)
    
    cursor.execute(sql, val)
    result = cursor.fetchall()

    for x in result:
        if x[1] == username and x[2]==password:
            return static_file("home.html", root="views/")
        else:
            return "<p>Login failed.</p>"

@app.route("/logout")
def logout():
    return redirect("/login")


run(app, host="localhost", port=8080)
