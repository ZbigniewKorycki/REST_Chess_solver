from flask import Flask, jsonify
from figures import Bishop, King, Knight, Pawn, Queen, Rook

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_list_available_moves(chess_figure: str, current_field: str):
    figure_classes = {
        "bishop": Bishop,
        "king": King,
        "knight": Knight,
        "pawn": Pawn,
        "queen": Queen,
        "rook": Rook,
    }

    figure_class = figure_classes.get(chess_figure.lower())
    if not figure_class:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": "invalid figure",
                    "figure": chess_figure,
                    "currentField": current_field,
                }
            ),
            404,
        )

    figure_instance = figure_class(current_field)

    try:
        figure_instance.list_available_moves()
    except ValueError as e:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": str(e),
                    "figure": chess_figure,
                    "currentField": current_field,
                }
            ),
            409,
        )
    available_moves = figure_instance.list_available_moves()
    if chess_figure.lower() == "pawn":
        whites_moves = available_moves[0]["whites"]
        blacks_moves = available_moves[0]["blacks"]
        return (
            jsonify(
                {
                    "availableMoves": {
                        "forWhites": whites_moves if whites_moves is not None else [],
                        "forBlacks": blacks_moves if blacks_moves is not None else [],
                    },
                    "error": {
                        "forWhites": "invalid field for figure"
                        if whites_moves is None
                        else None,
                        "forBlacks": "invalid field for figure"
                        if blacks_moves is None
                        else None,
                    },
                    "figure": chess_figure,
                    "currentField": current_field,
                }
            ),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "availableMoves": available_moves,
                    "error": None,
                    "figure": chess_figure,
                    "currentField": current_field,
                }
            ),
            200,
        )


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    figure_classes = {
        "bishop": Bishop,
        "king": King,
        "knight": Knight,
        "pawn": Pawn,
        "queen": Queen,
        "rook": Rook,
    }

    figure_class = figure_classes.get(chess_figure.lower())
    if not figure_class:
        return (
            jsonify(
                {
                    "move": "invalid",
                    "figure": chess_figure,
                    "error": "invalid figure",
                    "currentField": current_field,
                    "destField": dest_field,
                }
            ),
            404,
        )
    figure_instance = figure_class(current_field)

    try:
        figure_instance.validate_move(dest_field)
    except ValueError as e:
        return (
            jsonify(
                {
                    "move": "invalid",
                    "figure": chess_figure,
                    "error": str(e),
                    "currentField": current_field,
                    "destField": dest_field,
                }
            ),
            409,
        )

    if chess_figure.lower() == "pawn":
        is_move_valid, move_info, error_info = figure_instance.validate_move(dest_field)
        return (
            jsonify(
                {
                    "move": move_info,
                    "figure": chess_figure,
                    "error": error_info,
                    "currentField": current_field,
                    "destField": dest_field,
                }
            ),
            200,
        )

    else:
        is_move_valid = figure_instance.validate_move(dest_field)
        return (
            jsonify(
                {
                    "move": "valid" if is_move_valid else "invalid",
                    "figure": chess_figure,
                    "error": None if is_move_valid else "current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }
            ),
            200,
        )


@app.errorhandler(500)
def handle_internal_server_error_500(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
