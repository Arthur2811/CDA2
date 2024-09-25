from flask import Flask
import mysql.connector
from mysql.connector import Error
from config import Config

# Création de l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Fonction pour se connecter à la base de données
def connect_db():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

# Exécution de l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
