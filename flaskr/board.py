"""
Carson Siegrist
12/18/2023
board.py

File takes care of all game board logic.
Including initializing board, updating board when play, and handling win conditions. 
"""

from enum import Enum

class TileState(Enum):
    Unoccupied = 0
    Occupied_Cathedral = 1
    Occupied_p1 = 2
    Occpuied_p2 = 3
    Zoned_p1 = 4
    Zoned_p2 = 5

class Tile:
    #Default constructor requires state
    def __init__(self, state):
        self.state = state

    #Convert to string for debugging purposes
    def __str__(self):
        return str(self.state)

    #Allow setting the state of a tile
    def setState(self, state):
        self.state = state


class Board: 
    BOARD_SIZE = 10 
    turnCount = 0
    

    #Create a BOARD_SIZE * BOARD_SIZE matrix made of tile objects defaulted to be unoccupied
    def __init__(self): 
        self.board = [[Tile(TileState.Unoccupied) for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]
        
    #String representation of board for debugging
    #Prints each tile's current state in a BOARD_SIZE x BOARD_SIZE grid
    def __str__(self):
        out = ""
        for row in self.board:
            for tile in row:
                out += f"{tile.state.value} "
            out += "\n"
        return out[:len(out):] #Don't return extra newline
    

    #-1 returned if move is invalid, otherwise board and turnCount is updated . 
    def play_piece(self, piece, coord, rotation):
        pass

    # Verifies is a piece is playable
    def is_playable(self, piece, coord, rotation):
        pass

    # Genertae coordinates piece will occupy. Returns -1 if piece would go off board.
    def generate_coordinates(self, piece, coord, rotation):
        pass


board = Board()
print()
print(board)