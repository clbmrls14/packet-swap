
NEW_GAME_BOARD = {
    (0,0):' ', (0,1):'O', (0,2):'O', (0,3):'O', (0,4):' ',
    (1,0):'X', (1,1):' ', (1,2):' ', (1,3):' ', (1,4):' ',
    (2,0):'X', (2,1):' ', (2,2):' ', (2,3):' ', (2,4):' ',
    (3,0):'X', (3,1):' ', (3,2):' ', (3,3):' ', (3,4):' ',
    (4,0):' ', (4,1):' ', (4,2):' ', (4,3):' ', (4,4):' '
}

class game_state:
    def __init__(self, turn: str = 'O', turn_count: int = 0, board: dict = NEW_GAME_BOARD):
        self.player_turn = turn
        self.num_turns = turn_count
        self.game_board = board
    
    def reset(self):
        self.player_turn = 'O'
        self.num_turns = 0
        self.game_board = NEW_GAME_BOARD

    def advance_packet(self, packet: tuple):
        if self.player_turn == 'O':
            x, y, turn, opponent = 1, 0, 'O', 'X'
        else:
            x, y, turn, opponent = 0, 1, 'X', 'O'
        if packet[0] == 4 or packet[1] == 4:
            return self
        destination = (packet[0]+x, packet[1]+y)
        hop_over = (packet[0]+(x*2), packet[1]+(y*2))
        if self.game_board[destination] == opponent and self.game_board[hop_over] == opponent:
            return self
        if self.game_board[destination] == ' ':
            self.game_board[destination] = turn
            self.game_board[packet] = ' '
            self.player_turn = opponent
        if self.game_board[destination] == opponent:
            if self.game_board[hop_over] == ' ':
                self.game_board[hop_over] = turn
                self.game_board[packet] = ' '
                self.player_turn = opponent
        return self

    def check_win_condition(self):
        x_win_condition = [(1,4), (2,4), (3,4)]
        o_win_condition = [(4,1), (4,2), (4,3)]
        if self.player_turn == 'X':
            if all(self.game_board[i] == self.player_turn for i in x_win_condition):
                return True
        if self.player_turn == 'O':
            if all(self.game_board == self.player_turn for i in o_win_condition):
                return True
        return False

    def print_board(board: dict):
        printer = ""
        for i in range(0,5):
            for j in range(0,5):
                printer = printer + " " + board[i,j]
            printer = printer + "\n"
        print(printer)
        return printer
