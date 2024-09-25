from flask import Flask
import getpass
import mysql.connector
from mysql.connector import Error

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = 'uimm'
    MYSQL_DB = 'guitare'

app = Flask(__name__)

def connect_bdd(password):
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=password,
            database=Config.MYSQL_DB
        )
        if connection.is_connected():
            print("Connexion réussie à la base de données")
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return None

def display_bdd(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM votre_table")  # Remplacez 'votre_table' par le nom de votre table
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()

def disconnect_bdd(connection):
    if connection.is_connected():
        connection.close()
        print("Déconnexion réussie de la base de données")

if __name__ == '__main__':
    pwd = getpass.getpass("Entrez le mot de la BDD MySQL: ")
    connection = connect_bdd(pwd)
    if connection:
        display_bdd(connection)
        disconnect_bdd(connection)
