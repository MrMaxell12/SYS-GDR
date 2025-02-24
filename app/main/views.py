from app.models.contas import Usuario
from . import main
from .. import db
from flask import jsonify, render_template, request, url_for, redirect, session


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
    # Recebe os dados de entrada do formulário
    username = request.form.get("username")
    senha = request.form.get("senha")

    # TODO: Usar hash da senha ao invés da senha em string.

    # Validar login
    # Procura usuário com nome enviado
    usuario = db.session.execute(db.select(Usuario).filter_by(username=username)).scalar_one()

    # Verificar se a senha bate
    if senha == usuario.senha:
        # Salva o usuário na sessão local e redireciona para a página principal
        session['username'] = username
        return redirect(url_for('main.main_route'))
    
    return render_template('login.html')


# Página de Cadastro
@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro_route():
    # Processar cadastro
    if request.method == 'POST':
        # Recebe os dados de entrada do formulário
        username = request.form.get("username")
        email = request.form.get("email")
        senha = request.form.get("senha")

        # Verificar se entradas estão presentes.
        if not all([ username, email, senha ]):
            # Cadastro inválido: faltando informações
            return render_template('cadastro.html')

        # Adiciona um novo usuário
        usuario = Usuario(username=username, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('main.login_route'))

    return render_template('cadastro.html')


# Página Principal do Usuário
@main.route('/main')
def main_route():
    # Se usuário não estiver logado, envie-o para a página inicial
    if not 'username' in session:
        return redirect(url_for('main.index_route'))

    return render_template('main.html', username=session['username'])


# Página de Status
@main.route('/status')
def status_route():
    return render_template('status.html')


# Página de Inventário
@main.route('/inventory')
def inventory_route():
    return render_template('inventory.html')

