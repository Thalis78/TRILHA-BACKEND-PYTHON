from exceptions import ErroValorInvalido

def eh_inteiro(valor):
    if not isinstance(valor, int):
        raise ErroValorInvalido("O valor informado não é um número inteiro")
    return True

def eh_float(valor):
    if not isinstance(valor, float):
        raise ErroValorInvalido("O valor informado não é um número flutuante")
    return True

def main():
    for valor in [10, "10"]:
        try:
            print(f"Verificando se '{valor}' é inteiro...")
            print("Resultado:", eh_inteiro(valor))
        except ErroValorInvalido as e:
            print("Erro:", e)

    print()  

    for valor in [10.5, 10]:
        try:
            print(f"Verificando se '{valor}' é float...")
            print("Resultado:", eh_float(valor))
        except ErroValorInvalido as e:
            print("Erro:", e)

if __name__ == "__main__":
    main()
