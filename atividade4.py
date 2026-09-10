from flask import Flask, jsonify, request

app = Flask(__name__)

musicas_bd = [
    {"id": 7, "nome": "Tempo achadex", "artista": "Legião Urbana", "ano": 1986},
    {"id": 2, "nome": "Pais e os fius", "artista": "Legião Urbana", "ano": 1989}
]

@app.route("/musicas")
def buscar_musicas():
    artista = request.args.get("artista")
    if artista:
        lista_retornar = []
        for musica in musicas_bd:
            if artista.lower() in musica["artista"].lower():
                lista_retornar.append(musica)
        return jsonify(lista_retornar)
    return jsonify(musicas_bd)

@app.route("/musicas/<int:id>")
def retornar_musica_por_id(id):
    for musica in musicas_bd:
        if id == musica["id"]:
            return jsonify(musica)
    return jsonify([])

app.run(debug=True)