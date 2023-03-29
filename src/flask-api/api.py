from flask import Flask,request
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"



