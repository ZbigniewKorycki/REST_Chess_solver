from flask import Flask, jsonify
from figures import Bishop, King, Knight, Pawn, Queen, Rook

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_list_available_moves(chess_figure, current_field):
    if chess_figure.lower() == "bishop":
        bishop = Bishop(current_field)
        available_moves = bishop.list_available_moves()
        if available_moves:
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
        else:
            return (
                jsonify(
                    {
                        "availableMoves": available_moves,
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )

    if chess_figure.lower() == "king":
        king = King(current_field)
        available_moves = king.list_available_moves()
        if available_moves:
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
        else:
            return (
                jsonify(
                    {
                        "availableMoves": available_moves,
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )
    if chess_figure.lower() == "knight":
        knight = Knight(current_field)
        available_moves = knight.list_available_moves()
        if available_moves:
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
        else:
            return (
                jsonify(
                    {
                        "availableMoves": available_moves,
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )
    if chess_figure.lower() == "pawn":
        pawn = Pawn(current_field)
        if not pawn.list_available_moves():
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
            pawn.list_available_moves()[0]["whites"]
        except KeyError:
            return jsonify(
                {
                    "availableMoves": {
                        "forWhites": [],
                        "forBlacks": []
                    },
                    "error": {
                        "forWhites": "invalid field, white pawn can not be on 1 row",
                        "forBlacks": None,
                    },
                    "figure": chess_figure,
                    "currentField": current_field,
                }, 409)
        try:
            pawn.list_available_moves()[0]["blacks"]
        except KeyError:
            return jsonify(
                {
                    "availableMoves": {
                        "forWhites": [],
                        "forBlacks": []
                    },
                    "error": {
                        "forWhites": None,
                        "forBlacks": "invalid field, black pawn can not be on 8 row",
                    },
                    "figure": chess_figure,
                    "currentField": current_field,
                }, 409)

        else:
            available_moves_for_whites = pawn.list_available_moves()[0]["whites"]
            available_moves_for_blacks = pawn.list_available_moves()[0]["blacks"]
            return (
                jsonify(
                    {
                        "availableMoves": {
                            "forWhites": available_moves_for_whites,
                            "forBlacks": available_moves_for_blacks,
                        },
                        "error": None,
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                200,
            )

    if chess_figure.lower() == "queen":
        queen = Queen(current_field)
        available_moves = queen.list_available_moves()
        if available_moves:
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
        else:
            return (
                jsonify(
                    {
                        "availableMoves": available_moves,
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )

    if chess_figure.lower() == "rook":
        rook = Rook(current_field)
        available_moves = rook.list_available_moves()
        if available_moves:
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
        else:
            return (
                jsonify(
                    {
                        "availableMoves": available_moves,
                        "error": "field does not exist",
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                ),
                409,
            )
    else:
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


if __name__ == "__main__":
    app.run(debug=True)
