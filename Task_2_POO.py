from Task_1_POO import Parser, Game

class Ranking:
    def __init__(self, parser):
        self.parser = parser
        self.total_kills_per_play = {}
        self.compute_total_kills()

    def compute_total_kills(self):
        for game in self.parser.games.values():
            for player, kills in game.kills.items():
                if player not in self.total_kills_per_play:
                    self.total_kills_per_play[player] = 0
                self.total_kills_per_play[player] += kills

    def print_ranking(self):
        sorted_players = sorted(
            self.total_kills_per_play.items(),
            key=lambda x: x[1],
            reverse = True
        )
        print("Ranking Geral de Kills: ")
        for i, (player, kills) in enumerate(sorted_players, 1):
            print(f"{i}. {player}: {kills}")

if __name__ == "__main__":
    parser = Parser("games.log")
    parser.parse()

    for game in parser.games.values():
        print(game)


    ranking = Ranking(parser)
    ranking.print_ranking()