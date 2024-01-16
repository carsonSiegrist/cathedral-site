from flask import Flask, render_template, jsonify, request
from game import Game


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    current_route = request.path
    return render_template("index.html", current_route = str(current_route))


# API for starting a new game
@app.route('/get_board', methods=['GET'])
def get_board():
    #create a board object
    #return board state as .json 
    return jsonify([
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    ])

#API for playing a move
#Returns current board state
@app.route('/play_move', methods=['POST'])
def play_move():
    #Take user input from the request 
    move_data = request.get_json()
    Game.play_move(move_data)
    pass

if __name__ == '__main__':
    app.run(debug=True)
