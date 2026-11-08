import os
import re
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.get("/usuario")
def buscar_usuario():
    nome = request.args.get("nome", "")
    conexao = sqlite3.connect("banco.db")
    consulta = "SELECT * FROM usuarios WHERE nome = ?"
    return str(conexao.execute(consulta, (nome,)).fetchall())


@app.get("/ping")
def ping():
    maquina = request.args.get("maquina", "")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", maquina):
        return "maquina invalida", 400
    subprocess.run(["ping", "-c", "1", maquina], check=False, capture_output=True, text=True)
    return "ping enviado"


if __name__ == "__main__":
    app.run(debug=True)
