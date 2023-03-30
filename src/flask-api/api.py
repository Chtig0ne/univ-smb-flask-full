from flask import Flask,render_template
import mydb.py
import mysql.connector


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, API!"

@app.route("/index.html")
def show_users():
 # Appeler la fonction pour récupérer les enregistrements de la base de données
    users = get_users()

    # Afficher les enregistrements dans une page HTML
    return render_template("index.html", users=users)
