games = {}
game_id = 0
current_game = None

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

        elif "Kill:" in line:
            parts = line.split("killed")
            
            killer = parts[0].rsplit(":",1)[1]
            victim = parts[1].split("by")[0]

            killer = killer.strip()
            victim = victim.strip()

            games[current_game]["total_kills"]+=1
                 
            players = games[current_game]["players"]
            kills = games[current_game]["kills"]

            if killer != "<world>":
                    if killer not in players:
                           players.append(killer)
                           kills[killer] = 0

                    
            if victim not in players:
                players.append(victim)
                kills[victim] = 0


            if killer != "<world>":
                 kills[killer] += 1
            else:
                kills[victim] -= 1
            
print(games)