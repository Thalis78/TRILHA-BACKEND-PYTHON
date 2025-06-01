class Game:
    def __init__(self,name = "",yearLaunch = 0,multiplayer = False,note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Game: {self.name}"
    
game1 = Game("Super Mario",2005,False,10)
game2 = Game("Fortnite",2017,False,10)

print("## DADOS DO JOGO ##")
print(f"\nNome do jogo: {game1.name}\nAno de lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de lançamento: {game2.yearLaunch}")