
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

    def piece_name(self):
        return self.name

    def verify_move(self, piece_pos, mov_pos, dest_empty): 
        return None 
    
class Pawn(Piece):
    white = "♟"
    black = "♙"
    name = "pawn"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
            piece_row_pos = piece_pos[0] 
            piece_col_pos = piece_pos[1] 
            mov_row_pos = mov_pos[0] 
            mov_col_pos = mov_pos[1] 
            row_offset = mov_row_pos - piece_row_pos
            col_offset = abs(mov_col_pos - piece_col_pos)
    
            mov_dir = -1 if self.check_color() == "white" else 1
            
            if ((row_offset == mov_dir and col_offset == 0) and dest_empty):
                return None
            if ((row_offset == mov_dir and col_offset == 1) and not dest_empty):
                return None
            #todo: ability to move twice from the starting position, en passant and promotion 
            
            return False
    
            '''this is how NOT to do it lol'''
            # if not (((row_offset == 1 and col_offset == 0) or dest_empty == True or self.check_color() == "white") and 
            #        ((row_offset == -1 and col_offset == 0) or dest_empty == True or self.check_color() == "black" ) and
            #        ((row_offset == 1 or col_offset == 1) or dest_empty == False or self.check_color() == "white") and
            #        ((row_offset == -1 or col_offset == -1) or dest_empty == False or self.check_color() == "black") or
            #        ((piece_row_pos == 2 and col_offset == 0) or piece_row_pos == 6 or dest_empty == True or self.check_color() == "white" or dest_empty == True or dest_empty == None) and
            #        ((piece_row_pos == -2 and col_offset == 0) or piece_row_pos == 1 or dest_empty == True or self.check_color() == "black" or dest_empty == True or dest_empty == None):
            #     return False
            

                

class Rook(Piece):
    white = "♜"
    black = "♖"
    name = "rook"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
            piece_row_pos = piece_pos[0] 
            piece_col_pos = piece_pos[1] 
            mov_row_pos = mov_pos[0] 
            mov_col_pos = mov_pos[1] 
            row_offset = abs(mov_row_pos - piece_row_pos)
            col_offset = abs(mov_col_pos - piece_col_pos)
            if not (row_offset == 0 or col_offset == 0):
                return False
            

class Knight(Piece):
    white = "♞"
    black = "♘"
    name = "knight"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
        piece_row_pos = piece_pos[0] 
        piece_col_pos = piece_pos[1] 
        mov_row_pos = mov_pos[0] 
        mov_col_pos = mov_pos[1] 
        row_offset = abs(mov_row_pos - piece_row_pos)
        col_offset = abs(mov_col_pos - piece_col_pos)
        if not ((row_offset == 1 and col_offset == 2) or (row_offset == 2 and col_offset == 1)):
            return False

        
class Bishop(Piece):
    white = "♝"
    black = "♗"
    name = "bishop"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
                piece_row_pos = piece_pos[0] 
                piece_col_pos = piece_pos[1] 
                mov_row_pos = mov_pos[0] 
                mov_col_pos = mov_pos[1] 
                row_offset = abs(mov_row_pos - piece_row_pos)
                col_offset = abs(mov_col_pos - piece_col_pos)
                if not (row_offset == col_offset):
                    return False
    
class Queen(Piece):
    white = "♛"
    black = "♕"
    name = "queen"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
            piece_row_pos = piece_pos[0] 
            piece_col_pos = piece_pos[1] 
            mov_row_pos = mov_pos[0] 
            mov_col_pos = mov_pos[1] 
            row_offset = abs(mov_row_pos - piece_row_pos)
            col_offset = abs(mov_col_pos - piece_col_pos)
            if not ((row_offset == 0 or col_offset == 0) or (row_offset == col_offset)):
                return False


class King(Piece):
    white = "♚"
    black = "♔"
    name = "king"

    def verify_move(self, piece_pos, mov_pos, dest_empty):
        piece_row_pos = piece_pos[0] 
        piece_col_pos = piece_pos[1] 
        mov_row_pos = mov_pos[0] 
        mov_col_pos = mov_pos[1] 
        row_offset = abs(mov_row_pos - piece_row_pos)
        col_offset = abs(mov_col_pos - piece_col_pos)
        if not (row_offset <= 1 and col_offset <= 1):
            return False
