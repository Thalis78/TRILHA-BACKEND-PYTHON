def dobrar(x):
   return x * 2

def map(funcao, lista):
    for i in range(len(lista)):
        lista[i] = funcao(lista[i])

def main():
    lista = [1,2,3,4,5]

    map(dobrar,lista)
    print(lista) # [2, 4, 6, 8, 10]

    map(lambda x: x // 2, lista)
    print(lista) # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()