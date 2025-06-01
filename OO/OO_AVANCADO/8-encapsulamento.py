class Game:
    def __init__(self,name = "",yearLaunch = 0,multiplayer = False,note = 0):
        self.__name = name
        self.__yearLaunch = yearLaunch
        self.__multiplayer = multiplayer
        self.__note = note

    def __str__(self):
        return f"Game: {self.__name}"
    
    def technical_sheet(self):
        print("## DADOS DO JOGO ##")
        print(f"Nome do jogo: {self.__name}")
        print(f"Modo Multiplayer?: {self.__multiplayer}")
        print(f"Ano de lançamento: {self.__yearLaunch}")
        print(f"Avaliação do jogo: {self.__note}\n")
    
    @property
    def name(self):
        return self.__name
    
    @property
    def yearLaunch(self):
        return self.__yearLaunch
    
    @property
    def multiplayer(self):
        return self.__multiplayer
    
    @property
    def note(self):
        return self.__note
    
    @name.setter
    def name(self,name):
        self.__name = name;

game1 = Game()
game1.name = "Fortnite"
print(game1)
    