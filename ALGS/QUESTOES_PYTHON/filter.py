def eh_par(x):
    return x % 2 == 0

def filter(funcao, lista):
    nova_lista = []
    for i in lista:
        if funcao(i):
            nova_lista.append(i)

    return nova_lista

def main():
    lista = [1,2,3,4,5,6]

    lista_numeros_pares = filter(eh_par,lista)
    print(lista_numeros_pares)

    lista_numeros_impares = filter(lambda x: x%2 != 0,lista)
    print(lista_numeros_impares)

if __name__ == "__main__":
    main()