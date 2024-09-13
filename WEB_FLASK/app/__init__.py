from flask import Flask

app = Flask(__name__)

# Import des routes pour enregistrer les endpoints
from app import routes