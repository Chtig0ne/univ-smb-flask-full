from flask import Flask
from flask import render_templates

app = Flask(__name__)

@app.route("/home")
def home():
    return render_templates('home.html')

@app.route('/about')
def about():
    return render_templates('about.html')

@app.route('/services')
def services():
    return render_templates('services.html')

@app.route('/contact')
def contact():
    return render_templates('contact.html')  