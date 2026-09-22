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
            print(f"{rank} {" ".join(symbols)} {rank}")
        print(" ".join(letters))

if __name__ == "__main__":
    
    test = Board()
    test.display_board()
