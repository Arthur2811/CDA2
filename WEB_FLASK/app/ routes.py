from app import app

@app.route('/')  # Décorator pour la page d'accueil
@app.route('/index')  # Décorator pour la page index
def index():
    strResult = 'Hello Bruz!'
    return strResult