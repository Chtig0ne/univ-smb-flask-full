from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('start.html')

@app.route("/index.html")
def index():
    return render_template("index.html")

