# self é uma referência ao próprio objeto que está sendo manipulado
# self funciona como um this;
class Carro:
    def __init__(self, nome, ano, modelo, valor):
        self.__nome = nome
        self.__ano = ano
        self.__modelo = modelo
        self.__valor = valor

    def get_nome(self):
        return self.__nome
    
    def get_ano(self):
        return self.__ano
    
    def get_modelo(self):
        return self.__modelo
    
    def get_valor(self):
        return self.__valor
    
    def set_nome(self,nome):
        self.__nome = nome
    
    def set_ano(self,ano):
        self.__ano = ano
    
    def set_modelo(self,modelo):
        self.__modelo = modelo
    
    def set_valor(self, valor):
        self.__valor = valor
    