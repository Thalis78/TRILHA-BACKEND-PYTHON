from models.Biblioteca import Biblioteca
from models.Livro import Livro
from models.Usuario import Usuario

def main():
    biblioteca = Biblioteca("Biblioteca Central")

    livro1 = Livro("Clean Code", "Robert C. Martin", 2008)
    livro2 = Livro("O Programador Pragmático", "Andrew Hunt", 1999)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    usuario = Usuario("Thalisson")
    biblioteca.registrar_usuario(usuario)

    while True:
        print("\n========= MENU =========")
        print("1. Mostrar livros disponíveis")
        print("2. Cadastrar novo livro")
        print("3. Cadastrar novo usuário")
        print("4. Emprestar livro para usuário")
        print("5. Devolver livro do usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca.mostrar_livros_disponiveis()
        
        elif opcao == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            novo_livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(novo_livro)

        elif opcao == "3":
            nome = input("Nome do usuário: ")
            novo_usuario = Usuario(nome)
            biblioteca.registrar_usuario(novo_usuario)

        elif opcao == "4":
            nome = input("Nome do usuário: ")
            usuario_encontrado = next((u for u in biblioteca._Biblioteca__usuarios if u._Usuario__nome.lower() == nome.lower()), None)
            if usuario_encontrado:
                biblioteca.emprestar_livro_para(usuario_encontrado)
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            nome = input("Nome do usuário: ")
            usuario_encontrado = next((u for u in biblioteca._Biblioteca__usuarios if u._Usuario__nome.lower() == nome.lower()), None)
            if usuario_encontrado:
                biblioteca.receber_livro_de(usuario_encontrado)
            else:
                print("Usuário não encontrado.")

        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
