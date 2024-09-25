import mysql.connector
from mysql.connector import Error
import getpass
 
 
# VARIABLES GLOBALES
mydb = None
mycursor = None

#========================================================
 
def connect_bdd(pwd):
 
    global mydb, mycursor
    
    try:
    #Demander à l'utilisateur son user et son password
 
        mydb = mysql.connector.connect(
            
            host="localhost",
            user= "root",
            password= pwd
        )
        return True
    except mysql.connector.Error:
            print("===================")
            print(f"Erreur de connexion, relancez le  programme")
            return False
 
def display_bdd():
     
    global mydb, mycursor
 
    mycursor = mydb.cursor()
    print("")
 
    # Utiliser la base de données choisie
    mycursor.execute(f"USE guitare")
 
    # Afficher les données de la table choisie
    mycursor.execute(f"SELECT * FROM nombre")
 
    print(f"Données dans la table client :")
 
    print("==============")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
 
    print("==============")
 
def disconnect_bdd():
     
    global mydb, mycursor
 
    mycursor.close()
    mydb.close()
    print("Fermeture de la connexion MySQL")    
 
#===========================================================================
 
if __name__ == "__main__":
    pwd = getpass.getpass("Entrez le mot de passe de la BDD MySQL: ")
    if connect_bdd(pwd):
        display_bdd()
        disconnect_bdd()
 