class ErroValorInvalido(Exception):
    def __init__(self,mensagem = "Valor inválido!"):
        self.__mensagem = mensagem
        super().__init__(self.__mensagem)