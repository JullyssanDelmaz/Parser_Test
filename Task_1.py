games = {}
game_id = 0
current_game = None
count=0

with open("games.log", "r") as file:
    for line in file:

        if "InitGame" in line:
            game_id+=1
            current_game = f"game_{game_id}"
            games[current_game] = {
                "total_kills": 0,
                "players": [],
                "kills": {}
                }

        elif "Kill" in line:
            parts = line.split("killed")
            

            left = parts[0].rsplit(":", 1)
            right = parts[1].split("by")

            killer = parts[0].rsplit(":",1)[1]
            victim = parts[1].split("by")[0]

            games[current_game]["total_kills"]+=1

print(games)