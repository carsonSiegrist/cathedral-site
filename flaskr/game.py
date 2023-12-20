"""
Carson Siegrist
12/19/2023
board.py

File actually runs the game, maintaining a board object and making calls to it as appropriate when input is provided. 
"""
from board import Board

turn = 0

class Game:
    
    #Create board object, return the array representation of it. 
    def startGame(self):
        self.board = Board()
        return self.board.board
    
    