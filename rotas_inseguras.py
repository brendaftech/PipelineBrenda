import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.get("/usuario")
def buscar_usuario():
    nome = request.args.get("nome", "")
    conexao = sqlite3.connect("banco.db")
    consulta = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    return str(conexao.execute(consulta).fetchall())


@app.get("/ping")
def ping():
    maquina = request.args.get("maquina", "")
    os.system("ping -c 1 " + maquina)
    return "ping enviado"


if __name__ == "__main__":
    app.run(debug=True)
