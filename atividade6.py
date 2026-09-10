from flask import Flask, jsonify, request

app = Flask(__name__)

carros_bd = [
    {"id": 30, "modelo": "Corolla", "marca": "Toyota", "ano": 2022},
    {"id": 2, "modelo": "fuca preto", "marca": "Honda", "ano": 1567},
    {"id": 3, "modelo": "Onix", "marca": "Chevrolet", "ano": 2020}
]

@app.route("/carros")
def buscar_carros():
    marca = request.args.get("marca")
    if marca:
        lista_retornar = []
        for carro in carros_bd:
            if marca.lower() in carro["marca"].lower():
                lista_retornar.append(carro)
        return jsonify(lista_retornar)
    return jsonify(carros_bd)

@app.route("/carros/<int:id>")
def retornar_carro_por_id(id):
    for carro in carros_bd:
        if id == carro["id"]:
            return jsonify(carro)
    return jsonify([])

app.run(debug=True)