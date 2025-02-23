from app import create_app
from app import db

# Cria o App
app = create_app('default')


# Inicia o banco de dados
with app.app_context():
    db.create_all()


# Inicia o App
if __name__ == "__main__":
    app.run()

