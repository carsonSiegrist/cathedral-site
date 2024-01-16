from flask import Flask, render_template, jsonify, request
from game import Game


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    title = "Cathedral"
    content = "Hello world!"
    return render_template("index.html", title=title, content=content)

# API for starting a new game
@app.route('/start_game')
def start_game():
    game = Game()
    game.start_game()
    return game.get_board()

#API for getting the current board
@app.route('/get_board', methods = ['GET'])
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
