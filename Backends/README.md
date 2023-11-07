# Backend

- [pycine (fastapi)](https://github.com/fscheidt/pycine)
- [front (svelte)](https://github.com/fscheidt/front)
- [web4 - 2023](https://github.com/fscheidt/web4-23)

## Configuração do ORM (SQLAlchemy)
- https://fastapi.tiangolo.com/pt/tutorial/sql-databases/

```bash
# Install framework ORM (sqlalchemy)
cd pycine
source env/bin/activate
pip install sqlalchemy
```

Para usar o sqlite no fastapi, precisamos definir os arquivos:
- crud.py
- database.py
- models.py
- schemas.py

Salvar configurações do projeto no requirements.txt:
```bash
cd pycine
pip freeze > requirements.txt
```

Ao iniciar o uvicorn, verificar se o arquivo `pycine.db` foi criado.

Testar: localhost:8000/docs



---

## Instalação do ambiente python

Setup inicial do ambiente de desenvolvimento:

```bash
# 1. criar pasta do projeto
# mkdir pycine
# cd pycine
# 2. criar ambiente virtual
python3 -m venv env
# 3. ativar ambiente virtual
source env/bin/activate
# 4. instalar dependências
pip install fastapi uvicorn requests
code .
```

## iniciar servidor fastapi

```bash
uvicorn pycine:app --reload
```

---

<details>
<summary><b>Utilitários</b></summary>

Teste de requisição com **httpie**


```bash
sudo apt-get install httpie
# ou
sudo snap install httpie
```

</details>