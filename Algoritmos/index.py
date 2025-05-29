def media(n1, n2):
    return (n1 + n2) / 2

def resultadoComIf(mediaFinal):
    if mediaFinal >= 7:
        return "APROVADO"
    elif mediaFinal >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def resultadoComTernario(mediaFinal):
    return (
        "APROVADO" if mediaFinal >= 7
        else "RECUPERAÇÃO" if mediaFinal >= 5
        else "REPROVADO"
    )

def resultadoComSwitch(mediaFinal):
    match mediaFinal:
        case n if n >= 7:
            return "APROVADO"
        case n if n >= 5:
            return "RECUPERAÇÃO"
        case _:
            return "REPROVADO"

def exemplo_loops():
    for i in range(5):
        print(i + 1)
    
    print()

    frutas = ['maçã', 'banana', 'laranjas']
    for fruta in frutas:
        print(fruta)
        print(i)
    
    print()

    for indice, fruta in enumerate(frutas):
        print(f"{indice}: {fruta}")

    print()

    pessoa = {'nome': 'João', 'idade': 30}
    for chave, valor in pessoa.items():
        print(f"{chave} = {valor}")

    print()

    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")

    print()

    nomes = ['Ana', 'Pedro', 'João']
    idades = [25, 30, 22]

    for nome, idade in zip(nomes, idades):
        print(f"{nome} tem {idade} anos")

    print()

    contador = 0
    while contador < 5:
        print(contador + 1)
        contador += 1
    else:
        print("FIM DO LOOP!")


def exemplo_arrays():
    numeros = [1,2,3,4,5]
    nomes = ['Ana', 'Pedro', 'João']

    numeros[0] = 20
    nomes.append("Thalisson")
    nomes.remove("João")

    print(nomes[2])
    print(numeros[0])

# EU NÃO PRECISO OBRIGATORIAMENTE ESPECIFICAR O TIPO DE EXCEÇÃO EM PYTHON PORÉM ISSO VAI DIFICULTAR O DEBUG.
def usandoExcecoes():
    try:
        numero = int (input("DIGITE UM  NÚMERO?"))
        print(numero)
    except:
        print("Você não digitou um número")
    finally:
        print("Programa finalizado!")

def main():
    exemplo_arrays()
main()
