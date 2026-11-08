from flask import Flask, jsonify, request

app = Flask(__name__)

ALUNOS = ["Ana", "Bruno", "Carla", "Daniel"]


@app.get("/")
def inicio():
    return jsonify(mensagem="Olá, Fatec! A pipeline está funcionando.")


@app.get("/alunos")
def listar_alunos():
    busca = request.args.get("nome", "").lower()
    resultado = [aluno for aluno in ALUNOS if busca in aluno.lower()]
    return jsonify(resultado)


if __name__ == "__main__":
    app.run()
