from flask import Flask, jsonify, render_template

from app.models.animal import Animal
from app.models.boa_constrictor import Boa_Constrictor
from app.models.gato import Gato
from app.models.huron import Huron
from app.models.perro import Perro


def create_app():
    app = Flask(__name__)

    animales = {
        "gato": Gato("Mishi", 3, 4.5),
        "perro": Perro("Firulais", 5, 12.0),
        "huron": Huron("Timon", 5, 3, "Estados Unidos", 10.5),
        "boa": Boa_Constrictor("Black Mamba", 8, 30, "Brasil", 15.5)
    }

    @app.route('/')
    def index():
        return render_template("index.html", animales=animales.keys())

    @app.route('/sonido/<animal>', methods=['GET'])
    def obtener_sonido(animal):
        if animal in animales:
            sonido = animales[animal].hacer_sonido() 
            return jsonify({"animal": animal, "sonido": sonido})
        return jsonify({"error": "Animal no encontrado"}), 404

    return app