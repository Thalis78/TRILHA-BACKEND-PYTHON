# O algoritmo Quick Sort é mais eficiente que o Bubble Sort na maioria dos casos,
# utilizando a técnica de dividir e conquistar para ordenar a lista.

def tamanho_lista(lista):
    return len(lista)

def mostrar_lista(lista):
    for i in lista:
        print(i)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = []
    maiores = []

    for item in lista[1:]:
        if item < pivo:
            menores.append(item)
        else:
            maiores.append(item)

    return quick_sort(menores) + [pivo] + quick_sort(maiores)

def main():
    lista = [5, 4, 3, 1, 2, 6]
    lista_ordenada = quick_sort(lista)
    mostrar_lista(lista_ordenada)

if __name__ == "__main__":
    main()
