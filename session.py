from board import Board


class Session:
    def __init__(self):
        self._active= True
        self._board = Board()
        self._message = ""

    def start_session(self):
        while self._active : 
            print("\033[2J\033[3J\033[H",end="") 
                           
            self._board.display_board()

            if not self._message == "":
                print(self._message)
                self._message = ""

            reply = input("move:")
            reply = reply.strip().lower()

            if reply in ("exit","quit"):
                print("Game, Over")
                self._active= False 
                continue

            elif reply == "restart":
                 self._board = Board()
                 self._message = "Game restarted"
                 continue
            
            elif not self.validation(reply):
                continue

            piece_pos = reply[0:2]
            move_pos = reply[2:]

            action = self._board.move(piece_pos,move_pos)
            if action != None:
                self._message = action 
            
    def validation(self, text):
        letters=["a","b","c","d","e","f","g","h"]
        numbers = [str(x) for x in range (1,9,1)]
        if len(text) != 4:
            self._message = "move must be made with four valid characters ex:<a2a3>\n---------------------\ntype <exit> or <quit> to exit the game and <restart> to restart the game\n"
            return False
        elif text[0] not in letters or text[2] not in letters:
            self._message = "invalid position"
            return False
        elif text[1] not in numbers or text[3] not in numbers:
            self._message = "invalid position"
            return False
        else:
            return True



