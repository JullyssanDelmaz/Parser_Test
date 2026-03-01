class Game:
    def __init__(self, game_id):
        self.game_id = game_id               
        self.total_kills = 0
        self.players = []
        self.kills = {}

       
    def add_player(self, name):
        if name in self.players:
            return
        else:
            self.players.append(name)
            self.kills[name] = 0

    def register_kill(self, killer, victim):
        self.total_kills+=1

        self.add_player(victim)

        if killer != "<world>":
            self.add_player(killer)
            self.kills[killer] += 1
        else:
            self.kills[victim] -= 1

    def __str__(self):
        kills_str = ",\n      ".join([f'"{k}": {v}' for k, v in self.kills.items()])
        return (f'game_{self.game_id}: {{\n'
                f'      total_kills: {self.total_kills}; \n'
                f'      players: {self.players}\n'
                f'      kills:{{\n'
                f'      {kills_str}\n'
                f'      }}\n'
                f'  }}')
        
    def __repr__(self):
        return self.__str__()

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.games = {}

    def parse(self):
        current_game = None
        game_id = 0
        with open(self.file_path, "r") as file:
            for line in file:
                if "InitGame" in line:
                    game_id += 1
                    current_game = Game(game_id)
                    self.games[f"game_{game_id}"] = current_game

                if "Kill:" in line:
                    parts = line.split("killed")
            
                    killer = parts[0].rsplit(":",1)[1].strip()
                    victim = parts[1].split("by")[0].strip()


                    current_game.register_kill(killer, victim)


parser = Parser("games.log")
parser.parse()
for game_id, game in parser.games.items():
    print(f"{game_id}: {game}")