from flask import Flask, jsonify, request

app = Flask(__name__)

restaurantes_bd = [
    {"id": 60, "nome": "Cantina dos amigos amigaveis", "tipo": "italiano", "cidade": "Curitiba"},
    {"id": 2, "nome": "Pasta e trator", "tipo": "italiano", "cidade": "Cascavel"},
    {"id": 3, "nome": "Sabor da BR277", "tipo": "brasileiro", "cidade": "Quedex do Iguacux"}
]

@app.route("/restaurantes")
def buscar_restaurantes():
    tipo = request.args.get("tipo")
    if tipo:
        lista_retornar = []
        for restaurante in restaurantes_bd:
            if tipo.lower() in restaurante["tipo"].lower():
                lista_retornar.append(restaurante)
        return jsonify(lista_retornar)
    return jsonify(restaurantes_bd)

@app.route("/restaurantes/<int:id>")
def retornar_restaurante_por_id(id):
    for restaurante in restaurantes_bd:
        if id == restaurante["id"]:
            return jsonify(restaurante)
    return jsonify([])

app.run(debug=True)