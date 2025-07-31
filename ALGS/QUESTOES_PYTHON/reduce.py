def reduce(funcao, lista):
    acumulador = lista[0]
    for item in lista[1:]:
        acumulador = funcao(acumulador, item)
    return acumulador

def main():
    lista = [1, 2, 3, 4]
    valor_total = reduce(lambda x, y: x + y, lista)
    print(valor_total) 
    multiplicacao_total = reduce(lambda x, y: x * y, lista)
    print(multiplicacao_total)

if __name__ == "__main__":
    main()
