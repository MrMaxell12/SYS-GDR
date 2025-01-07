from . import main
from flask import render_template


""" WEB PAGE 
------------------------------------------""" 

# Página "Portal"
@main.route('/')
def index_route():
    return render_template('index.html')

# Página de Login
@main.route('/login', methods=['GET'])
def login_route():
    return render_template('login.html')

# Verificação de Login
@main.route('/login', methods=['POST'])
def login_verify():
    return 'hello'

# Página Principal do Usuário
@main.route('/main')
def main_route():
    return render_template('main.html')

# Página de Status
@main.route('/status')
def status_route():
    return render_template('status.html')

# Página de Inventário
@main.route('/inventory')
def inventory_route():
    return render_template('inventory.html')

