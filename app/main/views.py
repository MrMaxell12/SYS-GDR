from ..models import Personagem
from ..models import Usuario
from . import main
from .. import db
from flask import current_app, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..session_keys import SessionKeys as SK


def verificar_login(route):
    def wrapper():
        if not session.get(SK.USERNAME):
            return redirect('main.login_route')
        route()
    return wrapper


def get_usuario():
    if not session.get(SK.USERNAME):
        raise RuntimeError('Impossível encontrar usuário. Usuário não está logado')
    username = session.get(SK.USERNAME)
    return db.session.query(Usuario).filter_by(username=username).first()



""" WEB PAGE 
------------------------------------------""" 

# Página "Portal"
@main.route('/')
def index_route():
    return render_template('index.html')



# Página de Login 
@main.route('/login', methods=['GET', 'POST'])
def login_route():

    if request.method == 'GET':
        return render_template('login.html')

    # Recebe os dados de entrada do formulário
    username = request.form.get("username")
    senha = str(request.form.get("senha"))

    # Validar login
    # Procura usuário com nome enviado
    usuario = db.session.execute(db.select(Usuario).filter_by(username=username)).scalar_one()

    # Verificar se a senha bate
    if check_password_hash(usuario.senha, senha):
        # Salva o usuário na sessão local e redireciona para a página principal
        session[SK.USERNAME] = username
        return redirect(url_for('main.selecao_personagem_route'))
    
    return render_template('login.html')



# Página de Cadastro
@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro_route():
    # Servir a página no GET
    if request.method == 'GET':
        return render_template('cadastro.html')

    # Processar cadastro
    # Recebe os dados de entrada do formulário
    username = request.form.get("username")
    email = request.form.get("email")
    senha = str(request.form.get("senha"))

    hashed_senha = generate_password_hash(senha)

    # Verificar se entradas estão presentes.
    if not all([ username, email, senha ]):
        # Cadastro inválido: faltando informações
        return render_template('cadastro.html')

    # Adiciona um novo usuário
    usuario = Usuario(username=username, email=email, senha=hashed_senha)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('main.login_route'))




# Página de Criação de Personagem
@verificar_login
@main.route('/criacao_personagem', methods=['GET', 'POST'])
def criacao_personagem_route():
    # Renderiza a página
    if request.method == 'GET':
        return render_template('criacao_personagem.html')

    # Coleta os dados do personagem
    nome = request.form.get('nome')
    dono = db.session.query(Usuario).filter_by(username=session['username']).first()
    
    if not dono:
        raise RuntimeError('Usuário não existente')

    # Cria o personagem novo
    novo_personagem = Personagem(nome=nome, dono=dono)
    db.session.add(novo_personagem)
    db.session.commit()

    # Altera a sessão do jogador
    session[SK.SELECTED_CHARACTER] = novo_personagem.id

    # Redireciona para a página principal, caso só tenha um personagem
    if len(dono.personagens) == 1:
        return redirect(url_for('main.main_route'))
        
    # Redireciona para a página de seleção de personagem
    return redirect(url_for('main.character_selection_route'))



# Página de seleção de Personagem
@verificar_login
@main.route('/selecao_personagem', methods=['GET'])
def selecao_personagem_route():
    usuario = get_usuario()
    personagens = usuario.personagens

    # Se não houver personagens, redireciona para a página de criação de personagens
    if len(personagens) <= 0:
        return redirect(url_for('main.criacao_personagem_route'))
    return render_template('selecao_personagem.html', personagens=personagens)



# Página Principal do Usuário
@verificar_login
@main.route('/main')
def main_route():
    # Se usuário não estiver logado, envie-o para a página inicial
    if not 'username' in session:
        return redirect(url_for('main.index_route'))

    return render_template('main.html', username=session.get(SK.USERNAME))



# Página de Status
@verificar_login
@main.route('/status')
def status_route():
    return render_template('status.html')



# Página de Inventário
@verificar_login
@main.route('/inventory')
def inventory_route():
    return render_template('inventory.html')

