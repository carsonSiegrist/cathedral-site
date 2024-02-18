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
@app.route('/start_game', methods = ['POST'])
def start_game():
    global game
    game = Game()
    return jsonify({"message": "Game started"})

#API for getting the current board
@app.route('/get_board', methods = ['GET'])
def get_board():

    if not game:
        return jsonify({"error" : str(e)})
    
    board = game.get_board()
    board_dict = {"board" : board.get_board_lst()}
    return jsonify(board_dict)

#API for playing a move
#Returns current board state
@app.route('/play_move', methods=['POST'])
def play_move():
    try:
        if not game:
            raise RuntimeError("Game not started. Call /start_game first.")
        
        #Take user input from the request 
        move_data = request.get_json()
    
    except RuntimeError as e:
        print(f"Error processing move_data: {e}")
        return jsonify({"error:" : str(e)})
    
    return game.play_move(move_data)


@app.route('/get_inventories', methods=['GET'])
def get_inventories():
    
    #Check there is an active game
    if not game:
        print(f"Error: Game has not been started. Call /start_game first.")
        return jsonify({"error":"Game not started. Call /start_game first."})
    
    return jsonify({1 : game.p1_inventory,
                    2 : game.p2_inventory})



if __name__ == '__main__':
    app.run(debug=True)