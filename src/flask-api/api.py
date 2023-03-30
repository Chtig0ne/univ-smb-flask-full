from flask import Flask,request
import mydb.py

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

@app.route("/")
def get_():
    return



