from app import app
from flask import render_template

@app.route('/')  # Route pour la page d'accueil
def home():
    return render_template("home.html")

@app.route('/claviers')  # Route pour la page des claviers
def claviers():
    return render_template("claviers.html")

@app.route('/guitare')  # Route pour la page des guitares
def guitare():
    return render_template("guitare.html")

@app.route('/index')  # Correction de la route
def index():
    # Assurez-vous que ifOdoo est une instance d'une classe avec ces attributs
    strResult = f'Hello Bruz! Odoo Serveur: {ifOdoo.mErpIpAddr}:{ifOdoo.mErpIpPort} = {ifOdoo.mOdooVersion}'
    return strResult

