# CLASSE PAI (SUPER CLASSE) - GENERALISTA
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

# CLASSE DERIVADA (SUBCLASSE) - ESPECIALIZADA
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0,storyline = ""):
        super().__init__(name, yearLaunch, multiplayer = False, note = note)
        self.storyline = storyline
    
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")
    

mult_game = Game("Fortnite",2017,True, 8.0)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Last of Us 2", 2020,9.5, "Emocionante história de sobrevivência")
sing_game.technical_sheet()