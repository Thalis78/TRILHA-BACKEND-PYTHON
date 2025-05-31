# self é uma referência ao próprio objeto que está sendo manipulado
# self funciona como um this;
class Carro:
    def __init__(self, nome, ano, modelo, valor):
        self.__nome = nome
        self.__ano = ano
        self.__modelo = modelo
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def exibir_detalhes(self):
        return f"Carro: {self.nome}, Ano: {self.ano}, Modelo: {self.modelo}, Valor: R${self.valor:.2f}"