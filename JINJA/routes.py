from flask import render_template
from app import app
from app import ifOdoo
@app.route('/') # decorators
def home():
return render_template('home.html', user=ifOdoo.mErpUser)
@app.route('/index')
def index():
def fields():
return render_template('fields.html', liste=ifOdoo.mListFields)

strResult = f'Hello Bruz! Odoo Server : 
{ifOdoo.mErpIpAddr}:{ifOdoo.mErpIpPort}={ifOdoo.mOdooVersion}'
return strResult
