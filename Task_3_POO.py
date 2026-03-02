from fastapi import FastAPI, HTTPException
from Task_1_POO import Parser, Game

app = FastAPI()

parser = Parser("games.log")
parser.parse()


@app.get("/game/{game_id}")

def get_game(game_id: int):
    key = f"game_{game_id}"
    if key not in parser.games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = parser.games[key]
    return{
        "game_id": game.game_id,
        "total_kills": game.total_kills,
        "players": game.players,
        "kills": game.kills
    }


@app.get("/ranking")

def get_ranking():
    ranking = {}
    for game in parser.games.values():
        for player, kills in game.kills.items():
            ranking[player] = ranking.get(player, 0) + kills

    sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    print("RANKING CALCULADO:", sorted_ranking)

    return [{"player": player, "kills": kills} for player, kills in sorted_ranking]