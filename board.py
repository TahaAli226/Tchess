from pieces import Pawn,Rook,Knight,Bishop,Queen,King


class Board:
    def __init__(self):
        self.__grid = [[None for x in range(8)] for x in range(8)]
        
        self.place_pieces()
    def place_pieces(self):
        pieces = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        for index, piece in enumerate(pieces):
            self.__grid[0][index] = piece("black")
            self.__grid[7][index] = piece("white")
        for index in range(8):
            self.__grid[1][index] = Pawn("black") 
            self.__grid[6][index] = Pawn("white")

    def display_board(self):
        letters = [" ","a","b","c","d","e","f","g","h"]
        print(" ".join(letters))
        for index ,row in enumerate(self.__grid):
            symbols = []
            rank = 8 - index
            for cell in row:
                if cell is None:
                    symbols.append(".")

                else:
                    symbols.append(cell.shape())
            print(f"{rank} {' '.join(symbols)} {rank}")
        print(" ".join(letters))

    def translate(self,x_pos,y_pos):
        letters_map = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        numbers_map = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
        col = letters_map[x_pos] 
        row = numbers_map[y_pos]
        return row, col

    def check_square(self, mov_pos):
        row_mov_pos, col_mov_pos = mov_pos
        if self.__grid[row_mov_pos][col_mov_pos] == None:
            return True 
        else: 
            return False
        
    def move(self,p_pos, m_pos):
        piece_pos = self.translate(p_pos[0], p_pos[1])
        move_pos = self.translate(m_pos[0], m_pos[1])
        row_piece_pos, col_piece_pos = piece_pos
        row_mov_pos, col_mov_pos = move_pos
        check_mov = self.check_square(move_pos)
        if self.__grid[row_piece_pos][col_piece_pos] == None:
            return "Can't move what's not there"
        
        elif self.__grid[row_mov_pos][col_mov_pos] != None:
            if self.__grid[row_piece_pos][col_piece_pos].check_color() == self.__grid[row_mov_pos][col_mov_pos].check_color():
                return f"Illegal move can't take your own pieces"
        
        if self.__grid[row_piece_pos][col_piece_pos].verify_move(piece_pos, move_pos, check_mov) == False:
                return f"Illegal {self.__grid[row_piece_pos][col_piece_pos].piece_name()} move"

        self.__grid[row_mov_pos][col_mov_pos] = self.__grid[row_piece_pos][col_piece_pos]
        self.__grid[row_piece_pos][col_piece_pos] = None

        
            
