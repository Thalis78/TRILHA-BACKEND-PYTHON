class Game:
    def __init__(self,name = "",yearLaunch = 0,multiplayer = False,note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("## DADOS DO JOGO ##")
        print(f"Nome do jogo: {self.name}")
        print(f"Modo Multiplayer?: {self.multiplayer}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Avaliação do jogo: {self.note}\n")
    
class GameStudio:
    def __init__(self,name):
        self.name = name 
        self.games = []
    
    def add_game(self,game):
        self.games.append(game)
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print("Não existe nenhum jogo.")
        else:
            average_note = total_notes / num_games
            print(f"Avaliação média dos jogos do studio {self.name} : {average_note:.2f}")

game1 = Game("Super Mario",2005,False,10)
game2 = Game("Fortnite",2017,True,8.0)

studio = GameStudio("Awesone Games")

studio.add_game(game1)
studio.add_game(game2)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()