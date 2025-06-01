from .Livro import Livro
from .Usuario import Usuario

class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []
        self.__usuarios = []
    
    def adicionar_livro(self, livro):
        if livro not in self.__livros:
            self.__livros.append(livro)
            print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
        else:
            print("Este livro já está na biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario not in self.__usuarios:
            self.__usuarios.append(usuario)
            print(f"Usuário '{usuario._Usuario__nome}' registrado com sucesso.")
        else:
            print("Este usuário já está registrado.")

    def mostrar_livros_disponiveis(self):
        print(f"\n📚 LIVROS DISPONÍVEIS NA BIBLIOTECA '{self.__nome.upper()}':")
        disponiveis = [livro for livro in self.__livros if livro.disponivel]
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
        else:
            for livro in disponiveis:
                livro.mostrar_info()
    
    def emprestar_livro_para(self, usuario):
        self.mostrar_livros_disponiveis()
        nome_livro = input(f"\n{usuario._Usuario__nome}, digite o nome do livro que deseja emprestar: ").strip()

        for livro in self.__livros:
            if livro.titulo.lower() == nome_livro.lower():
                if livro.disponivel:
                    livro.emprestar()
                    usuario._Usuario__livro_emprestado.append(livro)
                    print(f"\nLivro '{livro.titulo}' emprestado com sucesso para {usuario._Usuario__nome}.")
                    return
                else:
                    print("\nEsse livro já está emprestado.")
                    return

        print("Livro não encontrado na biblioteca.")


    def receber_livro_de(self, usuario):
        if not usuario._Usuario__livro_emprestado:
            print(f"{usuario._Usuario__nome} não tem livros para devolver.")
            return

        usuario.listar_livros_emprestados()
        try:
            escolha = int(input("\nDigite o número do livro que deseja devolver: "))
            if 1 <= escolha <= len(usuario._Usuario__livro_emprestado):
                livro = usuario._Usuario__livro_emprestado.pop(escolha - 1)
                livro.devolver()
                print(f"\nLivro '{livro.titulo}' devolvido à biblioteca.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")