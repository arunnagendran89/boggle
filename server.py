from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route("/")     # have a simple home page at /
def home_page():
    return "Welcome to Boggle!"


@app.route("/games", methods=["GET"])    # get games
def get_games():
    games = [{"id": "1", "content": {}}, {"id": "2", "content": {}}]
    return jsonify(games)


@app.route("/games", methods=["POST"])    # create a game
def create_game():
    game = request.get_json()
    return jsonify(game)

