import os
def menu():
    return int(input(
        """
        -------- OPERADORES ARITMETICOS ----------
        | 1 -> ADIÇÃO
        | 2 -> SUBTRAÇÃO
        | 3 -> MULTIPLICAÇÃO
        | 4 -> DIVISÃO
        | ESCOLHA:"""))

def realizar_operacao(num,operacao,funcao):
    for i in range(1,11):
        print(f"{num} {operacao} {i} = {funcao(num,i)}")


def resultado_operacao():
    resultadoMenu = menu()

    num = int(input("ESCOLHA UM NÚMERO PARA TABUADA: "))

    limpar_terminal()

    print("----------- RESULTADO ----------------")

    match(resultadoMenu):
        case 1: 
            realizar_operacao(num,"+",somatoria)
        case 2:
            realizar_operacao(num,"-",subtracao)
        case 3:
            realizar_operacao(num,"*",multiplicacao)
        case 4:
            realizar_operacao(num,"/",divisao)



def divisao (n1, n2):
    return n1 / n2

def subtracao(n1,n2):
    return n1 + n2

def multiplicacao(n1,n2):
    return n1 * n2

def somatoria(n1,n2):
    return n1 + n2

def limpar_terminal():
    os.system("cls")


def main():
    print("Olá mundo!!")


if __name__ == "__main__":
    resultado_operacao()