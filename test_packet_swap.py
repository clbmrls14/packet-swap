from packet_swap import game_state

random_board = {
    (0,0):' ', (0,1):' ', (0,2):' ', (0,3):'O', (0,4):' ',
    (1,0):'X', (1,1):'O', (1,2):'O', (1,3):' ', (1,4):' ',
    (2,0):'X', (2,1):' ', (2,2):' ', (2,3):' ', (2,4):' ',
    (3,0):' ', (3,1):' ', (3,2):'X', (3,3):' ', (3,4):' ',
    (4,0):' ', (4,1):' ', (4,2):' ', (4,3):' ', (4,4):' '
}

winning_board = {
    (0,0):' ', (0,1):' ', (0,2):' ', (0,3):'O', (0,4):' ',
    (1,0):' ', (1,1):'O', (1,2):'O', (1,3):' ', (1,4):'X',
    (2,0):' ', (2,1):' ', (2,2):' ', (2,3):' ', (2,4):'X',
    (3,0):' ', (3,1):' ', (3,2):' ', (3,3):' ', (3,4):'X',
    (4,0):' ', (4,1):' ', (4,2):' ', (4,3):' ', (4,4):' '
}

def test_advance_packet():
    # Piece advances to empty space and is replaced with blank
    test_game = game_state()
    test_game = game_state.advance_packet(test_game, (0,3)) # O
    game_state.print_board(test_game.game_board)
    assert test_game.game_board[(1,3)] == 'O'
    assert test_game.game_board[(0,3)] == ' '
    # Piece can hop over a single piece
    test_game = game_state.advance_packet(test_game, (1,0)) # X
    test_game = game_state.advance_packet(test_game, (0,1)) # O
    game_state.print_board(test_game.game_board)
    assert test_game.game_board[(1,1)] == 'X'
    assert test_game.game_board[(2,1)] == 'O'
    # Piece cannot hop two pieces
    test_game = game_state.advance_packet(test_game, (1,1)) # X
    test_game = game_state.advance_packet(test_game, (0,2)) # O
    test_game = game_state.advance_packet(test_game, (3,0)) # X
    test_game = game_state.advance_packet(test_game, (1,2)) # O
    game_state.print_board(test_game.game_board)
    assert test_game.game_board[(2,3)] == ' '
    assert test_game.game_board[(2,0)] == 'X'

def test_check_win_condition():
    test_game = game_state()
    assert game_state.check_win_condition(test_game) == False
    test_game.game_board = winning_board
    test_game.player_turn = 'X'
    assert game_state.check_win_condition(test_game) == True