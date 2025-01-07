# SYS-GDR

## Sobre
SISTEMA RPG PARA O GDR

## Tutoriais

### Configurando o ambiente local

Após clonar o projeto localmente, é necessário configurar o seu ambiente local com as dependências necessárias para executar o projeto. Com mais detalhes, é preciso criar um ambiente virtual python (venv), instalar os pacotes python via pip, ativar a venv, e (futuramente) instalar o projeto como um pacote python.

Isso pode ser feito automaticamente pelo `make`, ou manualmente.

#### Processo via make

1. Executar
```
$ make setup
```

Caso não funcione, vá para o processo manual.

#### Processo manual

1. Criar o ambiente virtual python (venv):
```
$ python -m venv .venv
```
Obs.: Certifique-se de estar na raiz do projeto.

2. Ative a venv.

No linux:
```
$ source .venv/bin/activate
```

No windows:
```
$ .venv\Scripts\activate
```

Para desativar:
```
(.venv) $ deactivate
```

3. Baixar as dependências via pip:
```
(.venv) $ pip install -r requirements.txt
```

4. (Futuramente) Instalar o pacote da aplicação flask
```
(.venv) $ pip install .
```


### Instalando novas dependências pip

Para instalar uma nova dependência no projeto faça da seguinte maneira:

1. Verifique se a venv está ativada. Caso não, ative-a.


2. Instale a dependência pelo pip como faria normalmente. Ex: flask-sqlalchemy
```
pip install <nova dependência>
```

3. Obtenha a lista de dependências que estão sendo utilizadas na venv pelo `pip freeze` e copie a saída para o `requirements.txt`
```
pip freeze
```

ou, de maneira automatizada no linux, utilize `>` para redirecionar a saída ao `requirements.txt`
```
pip freeze > requirements.txt
```
