from flask import Flask
from app.odoo import IF_Odoo

app = Flask(__name__)
IF_Odoo=IF_Odoo("192.168.0.17","vitre","inter","inter")
IF_Odoo.connect()

# Importation des routes après la création de l'objet app
from app import routes
