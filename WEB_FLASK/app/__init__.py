from flask import Flask

app = Flask(__name__)

# Importation des routes après la création de l'objet app
from app import routes
