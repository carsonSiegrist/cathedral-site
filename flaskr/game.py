"""
Carson Siegrist
12/19/2023
board.py

File actually runs the game, maintaining a board object and making calls to it as appropriate when input is provided. 
All calls from user data end up here. Makes sure all relevant parts of other files are updated.
"""
from board import Board
import json

class Game:
    

    #Create board object, return the array representation of it. 
    def start_game(self):
        self.turn = 0
        self.player = 1
        self.board = Board()
        return self.board.board
    
    #PRE: Valid move data passed as JSON. Board object initialized 
    #POST: -1 outputted if error, or updated board passed as JSON
    def play_move(self, move):

        #open file
        with open(move, 'r') as file:
            move_data = json.load(file)
        
        #Extract data
        piece_name = move_data["piece"]
        rotation = move_data["rotation"]
        coordinate = tuple(move_data["coordinate"]) 

        #TODO: check player's inventory before playing piece

        if not self.board.is_playable(piece_name, coordinate, rotation, self.player, self.board):
            return -1

        #Move is valid, play it
        self.board.play_piece(piece_name, coordinate, rotation, self.player, self.board, self.turn)
        #TODO: update player's inventory
        self.update_player()
        self.turn += 1 

    
    def update_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
