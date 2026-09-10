from flask import Flask, jsonify, request

app = Flask(__name__)

produtos_bd = [
    {"id": 20, "nome": "Notebook", "preco": 3500.0, "categoria": "informatica"},
    {"id": 2, "nome": "Mouse", "preco": 80.0, "categoria": "informatica"},
    {"id": 3, "nome": "Cadeira Gamer", "preco": 900.0, "categoria": "móveis"}
]

@app.route("/produtos")
def buscar_produtos():
    categoria = request.args.get("categoria")
    if categoria:
        lista_retornar = []
        for produto in produtos_bd:
            if categoria.lower() in produto["categoria"].lower():
                lista_retornar.append(produto)
        return jsonify(lista_retornar)
    return jsonify(produtos_bd)

@app.route("/produtos/<int:id>")
def retornar_produto_por_id(id):
    for produto in produtos_bd:
        if id == produto["id"]:
            return jsonify(produto)
    return jsonify([])

app.run(debug=True)