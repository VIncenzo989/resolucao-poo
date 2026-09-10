from flask import Flask, jsonify, request

app = Flask(__name__)

jogos_bd = [
    {"id": 50, "nome": "The Witcher 3", "genero": "rpg", "ano": 2015},
    {"id": 2, "nome": "FIFA 976", "genero": "esporte", "ano": 2976},
    {"id": 3, "nome": "GTA V", "genero": "ação", "ano": 2013}
]

@app.route("/jogos")
def buscar_jogos():
    genero = request.args.get("genero")
    if genero:
        lista_retornar = []
        for jogo in jogos_bd:
            if genero.lower() in jogo["genero"].lower():
                lista_retornar.append(jogo)
        return jsonify(lista_retornar)
    return jsonify(jogos_bd)

@app.route("/jogos/<int:id>")
def retornar_jogo_por_id(id):
    for jogo in jogos_bd:
        if id == jogo["id"]:
            return jsonify(jogo)
    return jsonify([])

app.run(debug=True)