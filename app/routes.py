from app import app
from flask import render_template


""" WEB PAGE 
------------------------------------------""" 

# Página "Portal"
@app.route('/')
def index_route():
    return render_template('index.html')

# Página de Login
@app.route('/login')
def login_route():
    return render_template('login.html')

# Página Principal do Usuário
@app.route('/main')
def main_route():
    return render_template('main.html')

# Página de Status
@app.route('/status')
def status_route():
    return render_template('status.html')

# Página de Inventário
@app.route('/inventory')
def inventory_route():
    return render_template('inventory.html')

