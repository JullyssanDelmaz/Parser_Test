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

            