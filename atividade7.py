from flask import Flask, jsonify, request

app = Flask(__name__)

cidades_bd = [
    {"id": 40, "nome": "Curitiba", "estado": "parana", "populacao": 199922},
    {"id": 2, "nome": "Londrina", "estado": "parana", "populacao": 575377},
    {"id": 3, "nome": "Caiscaveu", "estado": "parana", "populacao": 438888}
]

@app.route("/cidades")
def buscar_cidades():
    estado = request.args.get("estado")
    if estado:
        lista_retornar = []
        for cidade in cidades_bd:
            if estado.lower() in cidade["estado"].lower():
                lista_retornar.append(cidade)
        return jsonify(lista_retornar)
    return jsonify(cidades_bd)

@app.route("/cidades/<int:id>")
def retornar_cidade_por_id(id):
    for cidade in cidades_bd:
        if id == cidade["id"]:
            return jsonify(cidade)
    return jsonify([])

app.run(debug=True)