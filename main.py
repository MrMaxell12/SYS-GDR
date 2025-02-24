import argparse
from app import create_app
from app import db

# Cria o App
app = create_app('default')


# Inicia o banco de dados
with app.app_context():
    db.create_all()


# Inicia o App
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema copiloto do mestre para o RPG Guardiões das Relíquias")
    parser.add_argument("-d", "--debug", action="store_true", help="Ativa o modo debug do aplicativo, para ser utilizado em desenvolvimento")

    args = parser.parse_args()

    app.run(debug=args.debug)

