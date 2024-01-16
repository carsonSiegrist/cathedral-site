"""
Carson Siegrist
12/19/2023
board.py

File actually runs the game, maintaining a board object and making calls to it as appropriate when input is provided. 
All calls from user data end up here. Makes sure all relevant parts of other files are updated.
"""
from board import Board
from inventory import Inventory
import json

class Game:
    

    #Create game object
    def __init__(self):
        self.turn = 0
        self.player = 1
        self.board = Board()
        self.p1_inventory = Inventory(1)
        self.p2_inventory = Inventory(2)
    
    def __str__(self):
        return str(self.board)

    #returns current board
    def get_board(self):
        return self.board
        
    
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


        #Special cases involving the cathedral
        if self.turn == 1 and piece_name != "cathedral":
            raise RuntimeError("First move must be playing the cathedral!")
        
        if self.turn > 1 and piece_name == "cathedral": 
            raise RuntimeError("Cathedral piece illegally played!")
        

        #set p_inv to track current inventory
        p_inv = self.p1_inventory if self.player == 1 else self.p2_inventory 
        
        if not p_inv.has_piece(piece_name):
            raise RuntimeError("Player cannot play piece they don't have")
            
        if not self.board.is_playable(piece_name, coordinate, rotation, self.player):
            raise RuntimeError("Illegal move submitted")

        #Move is valid, play it
        self.board.play_piece(piece_name, coordinate, rotation, self.player, self.turn)
        p_inv.remove_piece(piece_name)
        self.update_player()
        self.turn += 1 
        #TODO: check if the game ended

    
    def update_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1


