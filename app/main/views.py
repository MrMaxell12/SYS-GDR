from . import main
from flask import jsonify, render_template, request


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
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    # TODO: Usar hash da senha ao invés da senha completa.

    # Validar senha
    


    return jsonify({'usuario': usuario, 'senha': senha})

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

