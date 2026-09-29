from flask import Flask
from controllers.musica_controller import musica_controller

app = Flask(__name__)

app.register_blueprint(musica_controller)


@app.route("/")
def inicio():
    return {
        "message": "API-MUSICAS funcionando!"
    }


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )