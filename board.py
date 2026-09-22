class Board:
    def __init__(self):
        self.__grid = [[None for x in range(8)] for x in range(8)]

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
                    symbols.append(str(cell))
            print(f"{rank} {" ".join(symbols)} {rank}")
        print(" ".join(letters))

if __name__ == "__main__":
    
    test = Board()
    test.display_board()
    