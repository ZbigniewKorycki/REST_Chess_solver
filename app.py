from flask import Flask, jsonify, make_response
from figures import Bishop, King, Knight, Pawn, Queen, Rook


def create_app():
    new_app = Flask(__name__)
    return new_app


app = create_app()


def get_chess_figure_class(chess_figure: str):
    figure_classes = {
        "bishop": Bishop,
        "king": King,
        "knight": Knight,
        "pawn": Pawn,
        "queen": Queen,
        "rook": Rook,
    }

    figure_class = figure_classes.get(chess_figure.lower())
    if figure_class:
        return figure_class


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_list_available_moves(chess_figure: str, current_field: str):
    figure_class = get_chess_figure_class(chess_figure)
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
        available_moves = figure_instance.list_available_moves()
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
    else:
        if chess_figure.lower() == "pawn":
            whites_moves = available_moves[0]["whites"]
            blacks_moves = available_moves[0]["blacks"]
            return (
                jsonify(
                    {
                        "availableMoves": {
                            "forWhites": whites_moves
                            if whites_moves is not None
                            else [],
                            "forBlacks": blacks_moves
                            if blacks_moves is not None
                            else [],
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
    figure_class = get_chess_figure_class(chess_figure)
    if not figure_class:
        return (
            jsonify(
                {
                    "move": "invalid",
                    "error": "invalid figure",
                    "figure": chess_figure,
                    "currentField": current_field,
                    "destField": dest_field,
                }
            ),
            404,
        )

    figure_instance = figure_class(current_field)

    try:
        is_move_valid = figure_instance.validate_move(dest_field)
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
    else:
        if chess_figure.lower() == "pawn":
            (
                is_move_valid_for_whites,
                is_move_valid_for_blacks,
            ) = figure_instance.validate_move(dest_field)
            return (
                jsonify(
                    {
                        "move": {
                            "forWhites": "valid"
                            if is_move_valid_for_whites
                            else "invalid",
                            "forBlacks": "valid"
                            if is_move_valid_for_blacks
                            else "invalid",
                        },
                        "figure": chess_figure,
                        "error": {
                            "forWhites": None
                            if is_move_valid_for_whites
                            else (
                                "invalid field for figure"
                                if is_move_valid_for_whites is None
                                else "current move is not permitted"
                            ),
                            "forBlacks": None
                            if is_move_valid_for_blacks
                            else (
                                "invalid field for figure"
                                if is_move_valid_for_blacks is None
                                else "current move is not permitted"
                            ),
                        },
                        "currentField": current_field,
                        "destField": dest_field,
                    }
                ),
                200,
            )

        else:
            return (
                jsonify(
                    {
                        "move": "valid" if is_move_valid else "invalid",
                        "figure": chess_figure,
                        "error": None
                        if is_move_valid
                        else "current move is not permitted",
                        "currentField": current_field,
                        "destField": dest_field,
                    }
                ),
                200,
            )


@app.errorhandler(500)
def handle_internal_server_error_500(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


@app.errorhandler(404)
def handle_not_found_error_404(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(debug=False)
