import mysql.connector
import json

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="votre_nom_d'utilisateur",
  password="votre_mot_de_passe",
  database="identity"
)

# Récupération des données de la table 'users'
cursor = mydb.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

# Conversion des résultats en liste de dictionnaires
data = []
for row in results:
  d = {
    'id': row[0],
    'username': row[1],
    'password': row[2],
    'first_name': row[3],
    'last_name': row[4],
    'email': row[5],
    'phone': row[6],
    'birthdate': row[7].strftime('%Y-%m-%d')
  }
  data.append(d)

# Écriture des résultats dans un fichier JSON
with open('users.json', 'w') as f:
  json.dump(data, f, indent=2)
