class Game:
    total_game = 0 # Variável de classe para contar o número total de jogos

    def __init__(self,name = "",yearLaunch = 0,multiplayer = False,note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_game += 1
        self.evaluators = 1

    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("## DADOS DO JOGO ##")
        print(f"Nome do jogo: {self.name}")
        print(f"Modo Multiplayer?: {self.multiplayer}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Avaliação do jogo: {self.note}\n")
    
    def evaluate(self,note):
        self.note += note
        self.evaluators += 1
    
    def average(self):
        media = self.note / self.evaluators
        print(f"Média de nota do jogo '{self.name}': {media:.2f}")

game1 = Game("Super Mario",2005,False,10)
game2 = Game("Fortnite",2017,True,8.0)

game1.technical_sheet()
game1.evaluate(10.0)
game1.evaluate(5.0)
game1.average()

print(f"Total de jogos criados: {Game.total_game}")