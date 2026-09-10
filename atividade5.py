from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios_bd = [
    {"id": 15, "nome": "Carlooox", "cargo": "programador", "salario": 5000.0},
    {"id": 2, "nome": "Anex", "cargo": "programador", "salario": 5500.0},
    {"id": 3, "nome": "Beatrix", "cargo": "designer", "salario": 4500.0}
]

@app.route("/funcionarios")
def buscar_funcionarios():
    cargo = request.args.get("cargo")
    if cargo:
        lista_retornar = []
        for funcionario in funcionarios_bd:
            if cargo.lower() in funcionario["cargo"].lower():
                lista_retornar.append(funcionario)
        return jsonify(lista_retornar)
    return jsonify(funcionarios_bd)

@app.route("/funcionarios/<int:id>")
def retornar_funcionario_por_id(id):
    for funcionario in funcionarios_bd:
        if id == funcionario["id"]:
            return jsonify(funcionario)
    return jsonify([])

app.run(debug=True)