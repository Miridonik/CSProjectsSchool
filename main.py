from flask import Flask, render_template,request
import mysql.connector

def get_connect():
    return mysql.connector.connect(
        host="185.114.247.43",
        user="sch688_vvedenie",
        password="Qwerty123") 

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login_page.html")

@app.route("/registration")
def registration_page():
    return render_template("registration_page.html")

@app.route("/register_user",methods=["POST"])
def register_user():
    rqs = request.get_json()
    name = rqs['name']
    pass1 = rqs['pass1']
    mail = rqs['mail']
    connect = get_connect()
    cur = connect.cursor()
    # cur.execute("INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)")
    return "okey"

app.run()