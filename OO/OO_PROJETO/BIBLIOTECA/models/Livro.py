class Livro:
    livros = []

    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano 
        self.__disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"NOME DO LIVRO: {self.__titulo}"

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        self.__autor = valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self.__disponivel = valor

    def mostrar_info(self):
        status = "Sim" if self.__disponivel else "Não"
        print(f"\nLIVRO      : {self.__titulo}"
              f"\nAUTOR      : {self.__autor}"
              f"\nANO        : {self.__ano}"
              f"\nDISPONÍVEL : {status}")

    def emprestar(self):
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

    @classmethod
    def listar_livros_disponiveis(cls):   
        print("\n===== LIVROS DISPONÍVEIS =====")
        for livro in cls.livros:
            if livro.disponivel:
                livro.mostrar_info()

    @classmethod
    def listar_livros_indisponiveis(cls):
        print("\n===== LIVROS INDISPONÍVEIS =====")
        for livro in cls.livros:
            if not livro.disponivel:
                livro.mostrar_info()

    @classmethod
    def quantidade_livros(cls):
        return len(cls.livros)
