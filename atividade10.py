from flask import Flask, jsonify, request

app = Flask(__name__)

cursos_bd = [
    {"id": 70, "nome": "Análise e Desenvolvimento de Sistemas", "instituicao": "ifpr", "duracao": "2 anos"},
    {"id": 2, "nome": "Técnico em Informática", "instituicao": "ifpr", "duracao": "3 anos"},
    {"id": 3, "nome": "ajudante de limpador de servente de aura", "instituicao": "ifpr", "duracao": "4 anos"}
]

@app.route("/cursos")
def buscar_cursos():
    instituicao = request.args.get("instituicao")
    if instituicao:
        lista_retornar = []
        for curso in cursos_bd:
            if instituicao.lower() in curso["instituicao"].lower():
                lista_retornar.append(curso)
        return jsonify(lista_retornar)
    return jsonify(cursos_bd)

@app.route("/cursos/<int:id>")
def retornar_curso_por_id(id):
    for curso in cursos_bd:
        if id == curso["id"]:
            return jsonify(curso)
    return jsonify([])

app.run(debug=True)