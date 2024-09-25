from flask import Flask
import getpass
import mysql.connector
from mysql.connector import Error

# Configuration des paramètres de connexion à la base de données
MYSQL_HOST = 'localhost'
MYSQL_DB = 'guitare'

app = Flask(__name__)

def connect_bdd(user, password):
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=user,
            password=password,
            database=MYSQL_DB
        )
        if connection.is_connected():
            print("Connexion réussie à la base de données")
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return None

def display_bdd(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT quantity1, quantity2 FROM nombre LIMIT 50")  # Suppression de l'ID
    records = cursor.fetchall()
    for row in records:
        print(f"Quantity1: {row[0]}, Quantity2: {row[1]}")  # Affiche les valeurs de quantity1 et quantity2
    cursor.close()

def update_quantities(connection, new_quantity1, new_quantity2):
    cursor = connection.cursor()
    # Mettez à jour la première ligne trouvée (ou modifiez la logique selon vos besoins)
    query = "UPDATE nombre SET quantity1 = %s, quantity2 = %s LIMIT 1"  # Limiter à une seule mise à jour
    cursor.execute(query, (new_quantity1, new_quantity2))
    connection.commit()
    print(f"Quantités mises à jour : Quantity1 = {new_quantity1}, Quantity2 = {new_quantity2}")
    cursor.close()

def disconnect_bdd(connection):
    if connection.is_connected():
        connection.close()
        print("Déconnexion réussie de la base de données")

@app.route('/')
def home():
    return "Bienvenue sur le serveur Flask !"

if __name__ == "__main__":
    user = input("Entrez le nom d'utilisateur de la BDD MySQL: ")
    pwd = getpass.getpass("Entrez le mot de passe de la BDD MySQL: ")
    connection = connect_bdd(user, pwd)
    if connection:
        display_bdd(connection)
        
        # Demander à l'utilisateur de modifier les quantités
        new_quantity1 = int(input("Entrez la nouvelle valeur pour quantity1 : "))
        new_quantity2 = int(input("Entrez la nouvelle valeur pour quantity2 : "))
        
        # Mettre à jour les quantités dans la base de données
        update_quantities(connection, new_quantity1, new_quantity2)
        
        disconnect_bdd(connection)
