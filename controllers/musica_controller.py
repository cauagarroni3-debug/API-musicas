from flask import Blueprint, request, jsonify
from models.musica import MusicaModel


musica_controller = Blueprint(
    "musica_controller",
    __name__
)


@musica_controller.route("/musicas", methods=["GET"])
def listar_musicas():

    musicas = MusicaModel.get_all()

    return jsonify(musicas), 200


@musica_controller.route("/musicas/<int:id>", methods=["GET"])
def buscar_musica(id):

    musica = MusicaModel.get_by_id(id)

    if musica is None:
        return jsonify({
            "message": "Música não encontrada"
        }), 404

    return jsonify(musica), 200


@musica_controller.route("/musicas", methods=["POST"])
def cadastrar_musica():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "message": "JSON não informado"
        }), 400

    titulo = dados.get("titulo")
    artista = dados.get("artista")
    album = dados.get("album")
    genero = dados.get("genero")
    ano = dados.get("ano")
    duracao = dados.get("duracao")

    if not titulo:
        return jsonify({
            "message": "O campo 'titulo' é obrigatório"
        }), 400

    if not artista:
        return jsonify({
            "message": "O campo 'artista' é obrigatório"
        }), 400

    id_musica = MusicaModel.criar(
        titulo,
        artista,
        album,
        genero,
        ano,
        duracao
    )

    return jsonify({
        "id": id_musica,
        "message": "Música cadastrada com sucesso"
    }), 201


@musica_controller.route("/musicas/<int:id>", methods=["DELETE"])
def deletar_musica(id):

    musica = MusicaModel.get_by_id(id)

    if musica is None:
        return jsonify({
            "message": "Música não encontrada"
        }), 404

    MusicaModel.deletar(id)

    return jsonify({
        "message": f"Música {id} deletada com sucesso"
    }), 200

@musica_controller.route("/musicas/<int:id>", methods=["PUT"])
def atualizar_musica(id):

    musica = MusicaModel.get_by_id(id)

    if musica is None:
        return jsonify({
            "message": "Música não encontrada"
        }), 404

    dados = request.get_json()

    if not dados:
        return jsonify({
            "message": "JSON não informado"
        }), 400

    titulo = dados.get("titulo")
    artista = dados.get("artista")
    album = dados.get("album")
    genero = dados.get("genero")
    ano = dados.get("ano")
    duracao = dados.get("duracao")

    MusicaModel.atualizar(
        id,
        titulo,
        artista,
        album,
        genero,
        ano,
        duracao
    )

    return jsonify({
        "message": f"Música {id} atualizada com sucesso"
    }), 200