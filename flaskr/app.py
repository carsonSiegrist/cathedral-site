from flask import Flask, render_template, jsonify, request
from game import Game


app = Flask(__name__, static_url_path='/static')
game = None #Holds board object

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
    board = game.get_board()
    board_dict = {"board" : str(board)}
    return jsonify(board_dict)

#API for getting the current board
@app.route('/get_board', methods = ['GET'])
def get_board():
    if not game:
        raise RuntimeError("Game not started. Call /start_game first.")
    board = game.get_board()
    board_dict = {"board" : board}
    return jsonify(board_dict)

#API for playing a move
#Returns current board state
@app.route('/play_move', methods=['POST'])
def play_move():
    if not game:
        raise RuntimeError("Game not started. Call /start_game first.")
    #Take user input from the request 
    move_data = request.get_json()
    game.play_move(move_data)
    return

if __name__ == '__main__':
    app.run(debug=True)
