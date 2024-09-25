import mysql.connector
from mysql.connector import Error
import getpass

#========================================================

class IF_BDD:
    def __init__(self) -> None:
        print('##Constructor##')
        self.mydb = None
        self.mycursor = None

    def connect_bdd(self, pwd):
        try:
            'Connexion à la base MySQL'
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=pwd
            )
            if self.mydb.is_connected():
                print("Connexion réussie à la base de données MySQL")
                return True
        except Error as e:
            print("===================")
            print(f"Erreur de connexion : {e}")
            return False

    def display_bdd(self):
        if self.mydb is None:
            print("Pas de connexion à la base de données.")
            return

        self.mycursor = self.mydb.cursor()

        'Utiliser la base de données "guitare"'
        self.mycursor.execute("USE guitare")

        'Afficher les données de la table "nombre"'
        self.mycursor.execute("SELECT * FROM nombre")
        print("Données dans la table 'nombre' :")
        print("==============")
        rows = self.mycursor.fetchall()
        for row in rows:
            print(row)
        print("==============")

    def disconnect_bdd(self):
        if self.mycursor is not None:
            self.mycursor.close()
        if self.mydb is not None and self.mydb.is_connected():
            self.mydb.close()
            print("Fermeture de la connexion MySQL")

    def __del__(self):
        print('##Destructor##')

#========================================================

if __name__ == "__main__":
    pwd = getpass.getpass("Entrez le mot de passe de la BDD MySQL: ")
    ifBdd = IF_BDD()
    if ifBdd.connect_bdd(pwd):
        ifBdd.display_bdd()
        ifBdd.disconnect_bdd()
