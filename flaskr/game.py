"""
Carson Siegrist
12/19/2023
board.py

File actually runs the game, maintaining a board object and making calls to it as appropriate when input is provided. 
All calls from user data end up here. Makes sure all relevant parts of other files are updated.
"""
from board import Board
from inventory import Inventory
from flask import jsonify

class Game:
    

    #Create game object
    def __init__(self):
        self.turn = 1
        self.player = 1
        self.board = Board()
        self.p1_inventory = Inventory(1)
        self.p2_inventory = Inventory(2)
    
    def __str__(self):
        return str(self.board)

    #returns current board
    def get_board(self):
        return self.board
        
    
    #PRE: Valid move data passed as dictionary. Board object initialized 
    #POST: -1 outputted if error, or updated board passed as JSON
    def play_move(self, move):

        try:
            piece_name = move["piece"]
            rotation = int(move["rotation"])
            coordinate = move["coordinate"]
            coordinate =  tuple([int(coordinate[0]), int(coordinate[1])])


            #Special cases involving the cathedral
            if self.turn == 1 and piece_name != "cathedral":
                raise RuntimeError("First move must be playing the cathedral!")
            
            if self.turn > 1 and piece_name == "cathedral": 
                raise RuntimeError("Cathedral piece illegally played!")
            

            #player inventory: set p_inv to track current inventory
            p_inv = self.p1_inventory if self.player == 1 else self.p2_inventory
            #enemy inventory 
            e_inv = self.p2_inventory if self.player == 1 else self.p1_inventory
            
            if not p_inv.has_piece(piece_name):
                raise RuntimeError("Player cannot play piece they don't have")
                
            if not self.board.is_playable(piece_name, coordinate, rotation, self.player):
                raise RuntimeError("Illegal move submitted")

            #Move is valid, play it
            captures = self.board.play_piece(piece_name, coordinate, rotation, self.player, self.turn)
            p_inv.remove_piece(piece_name)
            
            if self.game_over():
                return jsonify({"message" : "Move successfully played",
                                "winner" : {self.get_winner()}})

            self.update_player() #someone can play, game is not over
            self.turn += 1
            for capture in captures:
                e_inv.add_piece(capture)
            return jsonify({"message" : "Move successfully played",
                            "winner" : 0})
 
            
        
        except RuntimeError as e:
            print(f"Error playing move: {e}")
            raise e #Raise again to propogate to caller 
     
    #Game ends when no one can play 
    def game_over(self):
        return not(self.can_play(1) or self.can_play(2))

    #Returns True if the player has any valid moves, False otherwise
    def can_play(self, player):
        #Function is brute force, worst case O(numPieces (max 16) * rotations (4) * boardSize (max 100) * pieceSize (max 6) = 38,400 operations)
        
        #Look at correct inventory
        p_inv = self.p1_inventory if self.player == 1 else self.p2_inventory 

        for p in p_inv.inventory: #piece 
            for r, row in enumerate(self.board.board):
                for c, tile in enumerate(row):
                    for rotation in range(4): #rotation 
                        if self.board.is_playable(piece=p, coord=(r,c), rotation=rotation, player=player):
                            return True
        return False
        
    # Winner is defined as player with least amount of "tiles" left in their inventory.
    # A tie is possible. Function DOES NOT check that the game has ended 
    def get_winner(self):
        if len(self.p1_inventory) > len(self.p2_inventory):
            return 2
        elif len(self.p1_inventory) < len(self.p2_inventory):
            return 1
        else:
            return -1


    #Assumes game is not over (someone can take a turn)
    def update_player(self): 
        if self.player == 1 and self.can_play(player=2):
            self.player = 2
        elif self.player == 2 and self.can_play(player=1):
            self.player = 1
        
        else:  
            raise RuntimeError("No player can play!")


