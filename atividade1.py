from flask import Flask, jsonify, request

app = Flask(__name__)

filmes_bd = [
    {"id": 1, "nome": "Matrix", "diretor": "Flávio", "ano": 2000},
    {"id": 2, "nome": "Nemo", "diretor": "André", "ano": 2006}
]

@app.route("/filmes2")
def buscarFilmes():
    return jsonify(filmes_bd)


@app.route("/filmes/<int:id>")
def retornar_filmes_por_id(id):
    for filme in filmes_bd:
        if id == filme["id"]:
            return jsonify(filme)
    return jsonify([])

@app.route("/filmes")
def buscar_filmes_por_nome():
    nome = request.args.get("nome")
    lista_retornar = []
    
    if nome:
        for filme in filmes_bd:
            if nome.lower() in filme["nome"].lower():
                lista_retornar.append(filme)
                
    return jsonify(lista_retornar)

app.run(debug=True)