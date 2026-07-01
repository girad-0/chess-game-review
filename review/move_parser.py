import chess
import chess.pgn
from .engine import analyze_position


def parse_pgn(pgn_file):
    """
    Parse a PGN file and return all game information.
    """

    game = chess.pgn.read_game(pgn_file)

    if game is None:
        return None

    board = game.board()

    review_data = {
        "white": game.headers.get("White"),
        "black": game.headers.get("Black"),
        "event": game.headers.get("Event"),
        "date": game.headers.get("Date"),
        "result": game.headers.get("Result"),
        "moves": []
    }

    move_number = 1

    for move in game.mainline_moves():

        player = "White" if board.turn == chess.WHITE else "Black"

        san = board.san(move)

        fen_before = board.fen()

        engine_result = analyze_position(fen_before)

        # Best move may be None in some positions
        if engine_result["best_move"] is not None:
            best_move = board.san(engine_result["best_move"])
        else:
            best_move = "-"

        board.push(move)

        fen_after = board.fen()

        review_data["moves"].append({
            "move_number": move_number,
            "player": player,
            "san": san,
            "fen_before": fen_before,
            "fen_after": fen_after,
            "evaluation": str(engine_result["score"]),
            "best_move": best_move,
        })

        if board.turn == chess.WHITE:
            move_number += 1

    return review_data