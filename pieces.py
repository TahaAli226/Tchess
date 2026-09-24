class Piece:
    def __init__(self,color):
        self._color = color 

    def shape(self):
        if self._color == "white":
            return self.white
        else:
            return self.black 

    def check_color(self):
        if self._color == "white":
            return "white"
        else: 
            return "black"
        
class Pawn(Piece):
    white = "♟"
    black = "♙"
class Rook(Piece):
    white = "♜"
    black = "♖"
class Knight(Piece):
    white = "♞"
    black = "♘"
class Bishop(Piece):
    white = "♝"
    black = "♗"
class Queen(Piece):
    white = "♛"
    black = "♕"
class King(Piece):
    white = "♚"
    black = "♔"
