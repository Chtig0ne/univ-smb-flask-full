from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('start.html')

@app.route("/")
def index():
    return render_template('index.hmtl')

