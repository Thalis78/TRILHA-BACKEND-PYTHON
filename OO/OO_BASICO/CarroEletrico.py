from Carro import Carro

class CarroEletrico(Carro):
    def __init__(self, nome, ano, modelo, valor, autonomia):
        super().__init__(nome, ano, modelo, valor)
        self.__autonomia = autonomia

    @property
    def autonomia(self):
        return self.__autonomia

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}, Autonomia: {self.autonomia} km"
