from flask import render_template, request, redirect, url_for, flash, session
from app import app, connect_db
from mysql.connector import Error

# Fonction pour récupérer tous les enregistrements
def get_all_records():
    try:
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inventory")
        records = cursor.fetchall()
        return records
    except Error as e:
        print(f"Erreur : {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vérification des informations d'identification
        if username == app.config['MYSQL_USER'] and password == app.config['MYSQL_PASSWORD']:
            session['logged_in'] = True
            flash('Connexion réussie !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Nom d’utilisateur ou mot de passe incorrect.', 'danger')
    
    return render_template('login.html')

# Route pour la page d'accueil
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    records = get_all_records()
    if records:
        return render_template("home.html", records=records)
    else:
        flash("Aucun enregistrement trouvé.", "warning")
        return render_template("home.html", records=[])

# Route pour la page des claviers
@app.route('/claviers')
def claviers():
    return render_template("claviers.html")

# Route pour la page des guitares
@app.route('/guitares')
def guitare():
    return render_template("guitare.html")

# Page de déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Déconnexion réussie.', 'info')
    return redirect(url_for('login'))

