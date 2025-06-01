from .Livro import Livro
class Usuario:
    usuarios = []
    id_user = 1

    def __init__(self, nome):
        self.__nome = nome
        self.__id_usuario = Usuario.id_user 
        self.__livro_emprestado = []
        Usuario.usuarios.append(self)
        Usuario.id_user += 1

    def __str__(self):
        return f"NOME DO USUÁRIO: {self.__nome}"
    
    def listar_livros_emprestados(self):
        if not self.__livro_emprestado:
            print(f"\n{self.__nome} não possui livros emprestados no momento.")
            return

        print(f"\nLivros emprestados por {self.__nome}:")
        for i, livro in enumerate(self.__livro_emprestado, start=1):
            print(f"{i}. {livro.titulo} ({livro.ano})")



    def emprestar_livro(self):  
        Livro.listar_livros_disponiveis()
        nome_livro = input("Informe o nome do livro que você deseja: ").strip()

        for livro in Livro.livros:
            if livro.titulo.lower() == nome_livro.lower():
                if livro.disponivel:
                    livro.emprestar()
                    self.__livro_emprestado.append(livro)
                    print(f"\nLivro '{livro.titulo}' emprestado com sucesso!")
                    return
                else:
                    print("\nEsse livro não está disponível.")
                    return

        print("\nLivro não encontrado.")

    
    def devolver_livro(self):
        if not self.__livro_emprestado:
            print("Você não tem livros emprestados.")
            return

        self.listar_livros_emprestados()

        try:
            escolha = int(input("\nDigite o número do livro que deseja devolver: "))
            if 1 <= escolha <= len(self.__livro_emprestado):
                livro = self.__livro_emprestado.pop(escolha - 1)
                livro.devolver()
                print(f"\nLivro '{livro.titulo}' devolvido com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    