"""
Carson Siegrist
12/19/2023
inventory.py

File contains piece data, and tracks players' remaining pieces. 
"""


"""
Dictionary containing piece data. 

key is the name of the piece

The value is a list of coordinates it occupies, added to the "important coordinate" 
Each one contains (0,0) because that represents the important coordinate itself. 

Note the abbey and academy are different for dark/light player. 
"""


#WIP! #TODO: Implement inventory functionality for each player
from copy import copy

class Inventory: 

    #Each piece that a player could have access to. 
    piece_data = {  
        "tavern-1"        : [(0,0)],
        "tavern-2"        : [(0,0)],
        "stable-1"        : [(0,0), (0, 1)],
        "stable-2"        : [(0,0), (0, 1)],
        "inn-1"           : [(0,0), (0,1), (1,1)],
        "inn-2"           : [(0,0), (0,1), (1,1)],
        "bridge"        : [(0,0), (0,1), (0,2)],
        "square"        : [(0,0), (0,1), (1,0), (1,1)],
        "abbey-dark"    : [(0,0), (0,1), (-1,1), (-1,2)],
        "abbey-light"   : [(0,0), (0,1), (1,1), (1,2)],
        "manor"         : [(0,0), (-1,1), (0,1), (1,1)],
        "tower"         : [(0,0), (0,1), (-1,1), (-1, 2), (-2,2)],
        "infirmary"     : [(0,0), (1,0), (0,1), (-1,0), (0,-1)],
        "castle"        : [(0,0), (-1,0), (-1,1), (-1,2), (0,2)],
        "academy-dark"  : [(0,0),(0,1),(0,2),(1,1),(-1,2)],
        "academy-light" : [(0,0),(0,1),(0,2),(-1,1),(1,2)],
        "cathedral"     : [(0,0),(0,1),(0,2),(0,3),(1,1),(-1,1)]
    }

    def __init__(self, player):
        #dark and light have different pieces. 
        #need to determine which inventory to give them
        self.inventory = set(self.piece_data.keys()) #inventory is a set, a player can only have one of each peice. 
        
        if player == 1:
            self.inventory.remove("abbey-dark")
            self.inventory.remove("academy-dark")
        
        elif player == 2:
            self.inventory.remove("abbey-light")
            self.inventory.remove("academy-light")
            self.inventory.remove("cathedral")

        
        else:
            raise ValueError("Invalid player number supplied for Inventory object")
        
        return
    
    #returns number of pieces a player has
    def __len__(self):
        return len(self.inventory)
    
    
    #returns boolean, if player has the given piece
    def has_piece(self, piece):
        return piece in self.inventory
    
    #remove a piece from player's inventory. player must have piece to remove it
    def remove_piece(self, piece):
        if piece not in self.inventory:
            raise RuntimeError("Cannot remove piece, inventory does not contain it")
        else:
            self.inventory.remove(piece)

    #add a piece to a player's inventory. cannot add a piece player already has1
    def add_piece(self, piece):
        if piece in self.inventory:
            raise RuntimeError("Cannot give piece, player already has it")
        else:
            self.inventory.add(piece)

    #return player's inventory
    def get_inv(self):
        return self.inventory

    #return the sum of the size of each piece in the player's inventory
    #used for calculating winner 
    def get_size(self):
        sum = 0
        for piece in self.inventory:
            sum += len(self.get_piece_data(piece))
        return sum

    #PRE: piece name passed 
    #POST: Returns a list of tuples containing piece data, or -1 on invalid input.
    @staticmethod
    def get_piece_data(piece):
        if piece not in Inventory.piece_data.keys():
            raise ValueError("Invalid piece in getPieceData()")
        return copy(Inventory.piece_data[piece])


    #Pre valid piece and rotation passed. (rotation 0-3 inclusive)
    @staticmethod
    def rotate_piece(piece, rotation):     


        output = Inventory.get_piece_data(piece)
        #clockwise
        match rotation:
            case 0: #0 degrees
                return output
            case 1: #90 degrees
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (y, -x)
                return output
            case 2: #180 degrees
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (-x, -y)
                return output
            case 3: #270 degrees
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (-y, x)
                return output        
            
            case _: #default case
                raise ValueError(f"invalid rotation value in rotatePiece(), {rotation}")
