# O algoritmo Bubble Sort (Ordenação por Bolha) possui complexidade de tempo O(n²),
# pois utiliza duas estruturas de repetição (loops aninhados) para ordenar os elementos.

# O Bubble Sort compara pares de elementos adjacentes e realiza a troca de posição
# sempre que eles estiverem fora de ordem (no caso de ordenação crescente).

def tamanho_lista(lista):
    return len(lista)

def mostrar_lista(lista):
   for i in lista:
      print(i)

def bubble_sort(lista):
    n  = tamanho_lista(lista)
    for i in range(n):
     for j in range(0, n - i - 1): 
         if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


   
def main():
    lista = [5,4,3,1,2,6]
    bubble_sort(lista)
    mostrar_lista(lista)
    pass


if __name__ == "__main__":
    main()