# api_fake.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/jugadores")
def jugadores():
    return jsonify([
        {"nombre": "Paolo Guerrero", "posición": "Delantero"},
        {"nombre": "Carlos Zambrano", "posición": "Defensa"}
    ])

if __name__ == "__main__":
    app.run(debug=True)
