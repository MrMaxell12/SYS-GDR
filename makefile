APP_NAME=
PORT=5000


# Detecta o sistema operacional
ifeq ($(OS),Windows_NT)
    VENV_PYTHON=.venv\Scripts\python.exe
    VENV_PIP=.venv\Scripts\pip.exe
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        VENV_PYTHON=.venv/bin/python
        VENV_PIP=.venv/bin/pip
    endif
endif

# Cria a venv e instala as dependências
setup:
	python -m venv .venv
	./$(VENV_PIP) install -r requirements.txt


# Executa o projeto
run:
	flask run --debug
	# ./.venv/bin/waitress-serve --host 127.0.0.1 --port $(PORT) $(APP_NAME):app


# Apaga a venv
clear_venv:
	@if [ -d ".venv" ]; then rm -r .venv; fi



# Configurações de Deploy
# ----------------------------

# Realiza o deploy
deploy:
	sudo chmod +x ./scripts/deploy.sh
	./scripts/deploy.sh

undeploy:
	sudo chmod +x ./scripts/undeploy.sh
	./scripts/undeploy.sh


# Configurações do Servico
# ----------------------------
SERVICE_NAME=autoupdate

service-reload:
	sudo systemctl daemon-reload

service-restart:
	sudo setenforce 0
	sudo systemctl restart $(SERVICE_NAME)
	sudo setenforce 1

service-status:
	systemctl status $(SERVICE_NAME)

