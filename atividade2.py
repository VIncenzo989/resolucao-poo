from flask import Flask, jsonify, request

app = Flask(__name__)

alunos_bd = [
    {"id": 5, "nome": "mathiex", "curso": "Informática", "idade": 20},
    {"id": 2, "nome": "Marix", "curso": "Engenharia", "idade": 22},
    {"id": 3, "nome": "japones bahiano", "curso": "Direito", "idade": 25}
]

@app.route("/alunos")
def buscar_alunos():
    nome = request.args.get("nome")
    if nome:
        lista_retornar = []
        for aluno in alunos_bd:
            if nome.lower() in aluno["nome"].lower():
                lista_retornar.append(aluno)
        return jsonify(lista_retornar)
    return jsonify(alunos_bd)

@app.route("/alunos/<int:id>")
def retornar_aluno_por_id(id):
    for aluno in alunos_bd:
        if id == aluno["id"]:
            return jsonify(aluno)
    return jsonify([])

app.run(debug=True)