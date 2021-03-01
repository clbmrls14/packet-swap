from fastapi import FastAPI

from packet_swap import game_state, NEW_GAME_BOARD

app = FastAPI()

global_game = game_state('O', 0, NEW_GAME_BOARD)

@app.get("/")
async def new_game():
    game_state.reset(global_game)
    result = { 
        "turn" : global_game.player_turn, 
        "turn_count" : global_game.num_turns, 
        "board" : game_state.print_board(global_game.game_board)
    }
    return result

@app.post("/checkforwin")
async def check_for_win():
    win = game_state.check_win_condition(global_game)
    return win

@app.post("/taketurn")
async def take_turn(packet: tuple):
    game = game_state.advance_packet(global_game, packet)
    result = { 
        "turn" : game.player_turn, 
        "turn_count" : game.num_turns, 
        "board" : game_state.print_board(game.game_board)
    }
    return result