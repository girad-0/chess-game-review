import chess
import chess.engine


ENGINE_PATH = "engine/stockfish.exe"


def analyze_position(fen):

    board = chess.Board(fen)

    with chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) as engine:

        info = engine.analyse(
            board,
            chess.engine.Limit(depth=15)
        )

    score = info["score"].white()

    best_move = info["pv"][0]

    return {
        "score": score,
        "best_move": best_move,
    }