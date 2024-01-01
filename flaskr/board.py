"""
Carson Siegrist
12/18/2023
board.py

File takes care of all game board logic.
Including initializing board, updating board when play, and handling win conditions. 
"""

from enum import Enum
from inventory import rotatePiece

class TileState(Enum):
    Unoccupied = 0
    Occupied_Cathedral = 1
    Occupied_p1 = 2
    Occpuied_p2 = 3
    Zoned_p1 = 4
    Zoned_p2 = 5

class Tile:
    #Default constructor, defaults state to unoccupied. 
    def __init__(self, state = 0): 
        self.state = state

    #Convert to string for debugging purposes
    def __str__(self):
        return str(self.state)

    #Allow setting the state of a tile
    def setState(self, state):
        self.state = state


class Board: 
    BOARD_SIZE = 10 

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
    

    #PRE: Valid move is provided as input
    #POST: Board is updated to display piece  
    def play_piece(self, piece, coord, rotation, player, board):
        #Does NOT validate moves. 
        to_play = self.generate_coordinates(piece, coord, rotation)

        #Determine what to set tiles to 
        playerState = None
        if player == 1:
            playerState = TileState.Occupied_p1
        elif player == 2:
            playerState = TileState.Occpuied_p2

        #Cathedral takes priority over player, unique case.
        if piece == "cathedral":
            playerState = TileState.Occupied_Cathedral

        #TODO: Implement logic for determining if a player zoned an area with their play. 
        #TODO: Update tiles that become zoned. 

        #Update board 
        for x, y in to_play:
            board.board[x][y].setState(playerState)

        return

    #POST: Returns a boolean represnetation of if the input move is legal
    def is_playable(self, piece, coord, rotation, player, board):
        #A player can play a piece on the board if every coordinate it occupies is either:
            #Unoccupied
            #Zoned by player
        acceptable = [TileState.Unoccupied]
        
        #Add player's zones to acceptable tiles to play on 
        if player == 1:
            acceptable.append(TileState.Zoned_p1)
        elif player == 2:
            acceptable.append(TileState.Zoned_p2)
        
        #Generate a list of cooridnates the piece would occupy
        to_play = self.generate_coordinates(piece, coord, rotation)

        for x, y in to_play:
            #Check coordinates are within bounds of board
            if x < 0 or x >= self.BOARD_SIZE or y < 0 or y >= self.BOARD_SIZE:
                return False
            
            #Check coordinates are unoccupied or zoned by player
            if board.board[x][y].state not in acceptable:
                return False
        
        #No errors found, acceptable play
        return True
            

    #POST: Returns -1 if coordinates cannot be generated, otherwise returns a list of coordinates stored as tuples. 
    def generate_coordinates(self, piece, coord, rotation):
        coordinates = rotatePiece(piece, rotation) #gives coordinates relative to central "coord"
        cen_x, cen_y = coord #central x and y
        for i, x, y in coordinates:
            coordinates[i][0] = x + cen_x #x coordinate
            coordinates[i][1] = y + cen_y #y coordinate

        return coordinates


board = Board()
print()
print(board)