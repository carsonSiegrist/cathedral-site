"""
Carson Siegrist
12/18/2023
board.py

File takes care of all game board logic.
Including initializing board, updating board when play, and handling win conditions. 
"""

from enum import Enum
from collections import deque
from inventory import Inventory
from copy import copy

class TileState(Enum):
    Unoccupied = 0
    Occupied_Cathedral = 1
    Occupied_p1 = 2
    Occupied_p2 = 3
    Zoned_p1 = 4
    Zoned_p2 = 5


debug = False

#state variable tracks if the tile is occupied by a piece, and who owns it, if it is unoccupied, or if it is player controlled.
#piece variable tracks the name of the piece. 
class Tile:
    #Default constructor, defaults state to unoccupied, piece to None. 
    def __init__(self, state = 0): 
        self.state = state
        self.piece = None 

    #Convert to string for debugging purposes
    def __str__(self):
        return str(self.state)

    #Allow setting the state of a tile
    def setState(self, state):
        self.state = state

    #Allow setting the pieceoccupying a  tile
    def setPiece(self, piece):
        self.piece = piece


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
    
    #clears the board, setting all tiles to unoccupied.
    #for testing purposes. does NOT reset game. 
    def clear_board(self):
        for r in self.board:
            for tile in r:
                tile.setPiece(None)
                tile.setState(TileState.Unoccupied)
        return


    #PRE: Valid move is provided as input
    #POST: Board is updated to display piece  
    def play_piece(self, piece, coord, rotation, player, turn):
        #Does NOT validate moves. 
        to_play = self.generate_coordinates(piece, coord, rotation)

        #Determine what to set tiles to 
        player_state = None
        if player == 1:
            player_state = TileState.Occupied_p1
            player_zone_state = TileState.Zoned_p1
        elif player == 2:
            player_state = TileState.Occupied_p2
            player_zone_state = TileState.Zoned_p2
        else:
            raise ValueError("Error: Illegal player argument in play_piece()")

        #Cathedral takes priority over player, unique case.
        if piece == "cathedral":
            player_state = TileState.Occupied_Cathedral

        #play piece before searching if it captured
        for x, y in to_play:
            self.board[y][x].setState(player_state)            
            self.board[y][x].setPiece(piece)            

        #Players may NOT capture pieces during their first turn. (Cathedral cannot capture a piece either) 
        #Don't bother checking for captures. 
        if turn <= 3:
            return

        captures = self.find_captures(player)


        for capture in captures: 
            if debug:
                print(capture)
            for x, y in capture: #list of captured coords
                curr_tile = self.board[y][x]
                curr_state = curr_tile.state
                curr_piece = curr_tile.piece

                #Piece should be returned to player's hand (unless its the Cathedral)
                if curr_state in [TileState.Occupied_p1, TileState.Occupied_p2, TileState.Occupied_Cathedral]:
                    if curr_piece != "cathedral":
                        #TODO: Return curr_piece to enemy_player's hand
                        pass
                    curr_piece = None #remove piece from board

                curr_tile.setState(player_zone_state)


        return
    
    #Helper function to play_move
    #Finds all the captured spaces, returns them as a list of coordinates that have become captured. 
    #Does NOT update board or return captured pieces to their appropriate inventories. 
    def find_captures(self, player):

        #Only the player captures land
        if player == 1:
            player_state = TileState.Occupied_p1
            enemy_states = [TileState.Occupied_p2, TileState.Occupied_Cathedral]

        elif player == 2:
            player_state = TileState.Occupied_p2
            enemy_states = [TileState.Occupied_p1, TileState.Occupied_Cathedral]
        
        else:
            raise ValueError("Error: Invalid player in find_captures()")



        captures = list() #tracks areas that should be captured. 
        seen = set() #Tracks every coordinate that has been checked.

        for r, row in enumerate(self.board):
            for c, cell in enumerate(row):
        
                 #Any unoccupied cell that hasn't been searched should be searched. 
                if (cell.state == TileState.Unoccupied or cell.state in enemy_states) and (c, r) not in seen:
                    if debug:
                        print()
                        print("!!!!")
                        print("NEW BFS!!")
                        print("starting at", c, r)
                        print("!!!!")
                        print()
                    #BFS, counting number of pieces from each player found (+ cathedral)
                    q = deque()
                    curr_seen = set() #Tracks every coordinate in current zone. As opposed to seen, which tracks ALL seen tiles.  
                    
                    pass_piece = None #Tracks ONE enemy piece to pass through while detecting zone. If more than one is detected, capture is impossible
                    found_enemy = False

                    q.appendleft((c,r))
                    seen.add((c,r))
                    curr_seen.add((c,r))
                    if self.board[c][r].state in enemy_states:
                        pass_piece = board.board[c][r].piece
                    while q:
                        coords = q.pop()
                        neighbors = self.generate_neighbors(coords)
                        for neighbor in neighbors:
                            #if tile is unoccupied, add to the queue. Otherwise track the piece

                            if neighbor in curr_seen:
                                continue                        

                            x, y = neighbor
                            curr_tile = board.board[y][x]
                            curr_state = curr_tile.state
                            curr_piece = curr_tile.piece

                            if curr_state == player_state:
                                pass #Don't add it.

                            elif curr_state == TileState.Unoccupied:
                                q.appendleft(neighbor)
                                seen.add(neighbor)
                                curr_seen.add(neighbor)

                            elif curr_state in enemy_states:
                                if debug:
                                    print()
                                    print("Searching an enemy state!")
                                    print("at:", x, y)
                                    print("state:", curr_state)
                                    print("piece:", curr_piece)
                                    print()

                                #Allow searching through one enemy piece. 
                                if pass_piece == None:
                                    pass_piece = curr_piece
                                    if debug:
                                        print("Found pass piece!")
                                        print("pass_piece:", pass_piece)
                                
                                if pass_piece == curr_piece:
                                    q.appendleft(neighbor)
                                    seen.add(neighbor)
                                    curr_seen.add(neighbor)
                            
                                else: #Second enemy piece found.
                                    if debug:
                                        print("Enemy found!")
                                    found_enemy = True

                            else: #enemy controlled land.
                                #possible to take, provided the enemy only used one piece for the capture. (against edge)
                                q.appendleft(neighbor)
                                seen.add(neighbor)
                                curr_seen.add(neighbor)
                                pass

                    if not found_enemy:
                        capture = copy(curr_seen)
                        captures.append(capture)

                        if debug:
                            print("ZONE FOUND!")
                            print("Zone: ", capture)
 
        return captures

    #Generates a list of all in-bound coordinates surrounding an input coordinate, in all 8 directions. 
    def generate_neighbors(self, coordinates):
        x, y = coordinates
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]
        output = []
        for x, y in neighbors:
            xinBounds = x < self.BOARD_SIZE and x >= 0
            yinBounds = y < self.BOARD_SIZE and y >= 0
            if xinBounds and yinBounds:
                output.append((x, y))
        return output

    #POST: Returns a boolean represnetation of if the input move is legal
    def is_playable(self, piece, coord, rotation, player,):
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
            if self.board[y][x].state not in acceptable:
                return False
        
        #No errors found, acceptable play
        return True
            
    #Converts relative piece coordinates to actual coordinates on the board.
    #POST: Returns -1 if coordinates cannot be generated, otherwise returns a list of coordinates stored as tuples. 
    def generate_coordinates(self, piece, coord, rotation):
        coordinates = Inventory.rotatePiece(piece, rotation) #gives coordinates relative to central "coord"
        cen_x, cen_y = coord #central x and y
        for i, coords in enumerate(coordinates):
            x, y = coords
            coordinates[i] = (x + cen_x, y + cen_y)

        return coordinates

