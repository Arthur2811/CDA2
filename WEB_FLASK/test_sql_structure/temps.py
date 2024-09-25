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

    def update_column_value(self, column_name, new_value):
        if self.mydb is None:
            print("Pas de connexion à la base de données.")
            return

        try:
            self.mycursor = self.mydb.cursor()

            'Utiliser la base de données "guitare"'
            self.mycursor.execute("USE guitare")

            'Vérifier si la colonne existe'
            valid_columns = ['quantity1', 'quantity2', 'quantity3']
            if column_name not in valid_columns:
                print(f"Colonne invalide : {column_name}. Choisissez parmi {valid_columns}")
                return

            'Convertir la nouvelle valeur en entier'
            new_value = int(new_value)

            'Mettre à jour la colonne spécifiée avec la nouvelle valeur'
            update_query = f"UPDATE nombre SET {column_name} = %s"
            self.mycursor.execute(update_query, (new_value,))
            self.mydb.commit()
            print(f"Valeur de la colonne '{column_name}' mise à jour avec succès à {new_value}.")
        except ValueError:
            print("La valeur fournie doit être un entier.")
        except Error as e:
            print(f"Erreur lors de la mise à jour de la colonne : {e}")

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

        'Mettre à jour la valeur d’une colonne'
        col = input("Entrez la colonne à mettre à jour (quantity1, quantity2, quantity3) : ")
        val = input(f"Entrez la nouvelle valeur pour {col} : ")
        ifBdd.update_column_value(col, val)

        ifBdd.disconnect_bdd()
