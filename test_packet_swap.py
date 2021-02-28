from packet_swap import game_state

random_board = {
    (0,0):' ', (0,1):' ', (0,2):' ', (0,3):'O', (0,4):' ',
    (1,0):'X', (1,1):'O', (1,2):'O', (1,3):' ', (1,4):' ',
    (2,0):'X', (2,1):' ', (2,2):' ', (2,3):' ', (2,4):' ',
    (3,0):' ', (3,1):' ', (3,2):'X', (3,3):' ', (3,4):' ',
    (4,0):' ', (4,1):' ', (4,2):' ', (4,3):' ', (4,4):' '
}

def print_board(board: dict):
    printer = ""
    for i in range(0,4):
        for j in range(0,4):
            printer = printer + " " + board[i,j]
        printer = printer + "\n"
    print(printer)

def test_advance_packet():
    # Piece advances to empty space and is replaced with blank
    test_game = game_state()
    test_game = game_state.advance_packet(test_game, (0,3)) # O
    print_board(test_game.game_board)
    assert test_game.game_board[(1,3)] == 'O'
    assert test_game.game_board[(0,3)] == ' '
    # Piece can hop over a single piece
    test_game = game_state.advance_packet(test_game, (1,0)) # X
    test_game = game_state.advance_packet(test_game, (0,1)) # O
    print_board(test_game.game_board)
    assert test_game.game_board[(1,1)] == 'X'
    assert test_game.game_board[(2,1)] == 'O'
    # Piece cannot hop two pieces
    test_game = game_state.advance_packet(test_game, (1,1)) # X
    test_game = game_state.advance_packet(test_game, (0,2)) # O
    test_game = game_state.advance_packet(test_game, (3,0)) # X
    test_game = game_state.advance_packet(test_game, (1,2)) # O
    print_board(test_game.game_board)
    assert test_game.game_board[(2,3)] == ' '
    assert test_game.game_board[(2,0)] == 'X'