from flask import Flask, jsonify
from figures import Bishop, King, Knight, Pawn, Queen, Rook

app = Flask(__name__)


def get_figure_response(figure: str, current_field: str, available_moves: list):
    if available_moves:
        return (
            jsonify(
                {
                    "availableMoves": available_moves,
                    "error": None,
                    "figure": figure,
                    "currentField": current_field,
                }
            ),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": "field does not exist",
                    "figure": figure,
                    "currentField": current_field,
                }
            ),
            409,
        )


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

    if chess_figure.lower() == "pawn":
        available_moves = figure_instance.list_available_moves()
        if not available_moves:
            return (
                jsonify(
                    {
                        "availableMoves": [],
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )
        try:
            whites_moves = available_moves[0]["whites"]
            blacks_moves = available_moves[0]["blacks"]
        except KeyError:
            return (
                jsonify(
                    {
                        "availableMoves": {"forWhites": [], "forBlacks": []},
                        "error": {
                            "forWhites": "invalid field"
                            if "whites" not in available_moves[0]
                            else None,
                            "forBlacks": "invalid field"
                            if "blacks" not in available_moves[0]
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
                        "availableMoves": {
                            "forWhites": whites_moves,
                            "forBlacks": blacks_moves,
                        },
                        "error": None,
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                200,
            )

    else:
        available_moves = figure_instance.list_available_moves()
        return get_figure_response(chess_figure, current_field, available_moves)


@app.errorhandler(500)
def handle_internal_server_error_500(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
