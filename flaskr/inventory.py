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
    pieces = {  
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

    #PRE: piece name passed 
    #POST: Returns a list of tuples containing piece data, or -1 on invalid input.
    @staticmethod
    def getPieceData(piece):
        if piece not in Inventory.pieces.keys():
            raise ValueError("Invalid piece in getPieceData()")
        return copy(Inventory.pieces[piece])


    #Pre valid piece and rotation passed. (rotation 0-3 inclusive)
    @staticmethod
    def rotatePiece(piece, rotation):     

        output = Inventory.getPieceData(piece)
        match rotation:
            case 0:
                #no rotation requested
                return output
            case 1:
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (-y, x)
                return output
            case 2:
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (-x, -y)
                return output
            case 3:
                for i, coord in enumerate(output):
                    x, y = coord
                    output[i] = (y, -x)
                return output        
            
            case _: #default case
                raise ValueError("invalid rotation value in rotatePiece()")
