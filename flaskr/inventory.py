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
class Pieces: 

    
    pieces = {  
        "tavern"        : [(0,0)],
        "stable"        : [(0,0), (0, 1)],
        "inn"           : [(0,0), (0,1), (1,1)],
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
    def getPieceData(self, piece):
        if piece not in Pieces.pieces.keys():
            return -1
        return Pieces.pieces[piece]

    #Pre valid piece and rotation passed. (rotation 0-3 inclusive)
    def rotatePiece(self, piece, rotation):
        output = self.getPieceData(piece)
        
        if output == -1:
            return output
        
        match rotation:
            case 0:
                #no rotation requested
                return output
            case 1:
                for i, x, y in enumerate(output):
                    output[i][0] = -y
                    output[i][1] = x
                return output
            case 2:
                for i, x, y in enumerate(output):
                    output[i][0] = -x
                    output[i][1] = -y
                return output
            case 3:
                for i, x, y in enumerate(output):
                    output[i][0] = y
                    output[i][1] = -x
                return output        
            case _: #default case
                return -1
