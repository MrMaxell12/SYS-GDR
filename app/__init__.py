from flask import Flask
# Importa a classe Flask do módulo flask para criar a aplicação web.

app = Flask(__name__)
# Instancia a aplicação Flask.

from app import routes

