from flask import Flask,render_template
import mydb.py
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

@app.route("/index.html")
 # Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)
    
# Exécution de la requête pour récupérer les enregistrements de la base de données
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Fermeture de la connexion à la base de données
db.close()

# Affichage des enregistrements dans une page HTML
return render_template('index.html') 



