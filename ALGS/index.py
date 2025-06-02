def media(n1, n2):
    return (n1 + n2) / 2

def resultado_com_if(mediaFinal):
    if mediaFinal >= 7:
        return "APROVADO"
    elif mediaFinal >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def resultado_com_ternario(mediaFinal):
    return (
        "APROVADO" if mediaFinal >= 7
        else "RECUPERAÇÃO" if mediaFinal >= 5
        else "REPROVADO"
    )

def resultado_com_switch(mediaFinal):
    match mediaFinal:
        case n if n >= 7:
            return "APROVADO"
        case n if n >= 5:
            return "RECUPERAÇÃO"
        case _:
            return "REPROVADO"

def exemplo_loops():
    # range é uma função que cria uma sequência de números, que pode ser percorrida com o laço for.
    
    # Lista numérica:
    # Exemplos de uso do range com uma, duas e três expressões:

    # range(5)
    # Apenas um valor é passado: 5 é o valor final (não incluso).
    # O início é 0 (padrão) e o passo é 1 (padrão).
    # Resultado: 0, 1, 2, 3, 4

    # range(5, 10)
    # Dois valores: 5 é o valor inicial, 10 é o valor final (não incluso).
    # O passo ainda é 1 (padrão).
    # Resultado: 5, 6, 7, 8, 9

    # range(5, 10, 2)
    # Três valores: 5 é o início, 10 é o fim (não incluso), e 2 é o passo.
    # Resultado: 5, 7, 9

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

def exemplo_set():
    # SET É UMA COLEÇÃO DE ITENS QUE NÃO PODEM SER DUPLICADOS.
    filmes_set = {"Inception",True,1,8.7}
    exemplo_set = {"Lincoln","Naty","Lucas"}

    filmes_set.add("Thalisson")
    filmes_set.update(exemplo_set)
    filmes_set.remove(1)

    print(len(filmes_set))
    print(filmes_set)

def exemplo_dicionario():
    # DICIONARIOS EM PYTHON SÃO SIMILARES A OBJETOS EM JS.
    # PODENDO SER QUALQUER TIPO IMUTAVEL
    filmInception = {
        "TITULO": "SENHOR DOS ANÉIS",
        "ANO" : 2024
    }

    filmInception["ANO"] = 2000
    filmInception["GENERO"] = "FICCAO"
    print(filmInception)
    print(filmInception["TITULO"])
    print(filmInception["ANO"])
    print(filmInception["GENERO"])
    print(filmInception.keys())
    print(filmInception.values())
    print(filmInception.items())

def list_comprehension():
    frutas = ['morango', 'banana', 'laranjas']

    frutas_with_a = [fruta for fruta in frutas if 'o' in fruta.lower()]
    frutas_diferente_de_morango = [fruta for fruta in frutas if fruta.lower() != 'morango']
    list_numbers = [i for i in range(10) if i < 4] 

    print(frutas_with_a)
    print(frutas_diferente_de_morango)
    print(list_numbers)

    print(f"\n======================================\n"
          f"{frutas}"
    )
    while True:
        escolha_uma_fruta = input("Digite um nome de uma fruta ou vazio para encerrar: ").lower()
        if escolha_uma_fruta == "":
            break
        
        frutas_escolhidas = [fruta for fruta in frutas if escolha_uma_fruta in fruta.lower()]

        print(f"FRUTAS ENCONTRADAS: {frutas_escolhidas}")

def funcoes_args_kwargs():
    # ARGS(*) É UTILIZADO QUANDO NÃO TENHO CERTEZA DE QUANTOS ARGUMENTOS IREMOS TER NA FUNÇÃO.
    # OS ARGUMENTOS SÃO PASSADOS COM UMA TUPLA

    # KWARGS(**) - ALÉM DOS VALORES PODEMOS PASSAR TAMBEM AS RESPECTIVAS CHAVES PARA CADA ARGUMENTO.
    # OS ARGUMENTOS SÃO PASSADOS COMO DINCIONARIO

    # EXEMPLOS USANDO ARGS:
    def sum(*num):
        sum_total = 0;
        for n in num:
            sum_total += n
        
        print(f"Soma é: {sum_total}\n")

    sum(7,2,3,4,5,6)

    # EXEMPLOS USANDO KWARGS:
    def apresenta_cursos(**data):
        for key, value in data.items():
            print(f"{key} - {value}")

        print()

    print(f"CURSOS DE PROGRAMAÇÃO: \n")
    apresenta_cursos(name = "JAVA", category = "BACKEND", level = "AVANCADO")
    apresenta_cursos(name = "JS", category = "FRONTEND", level = "INICIANTE")

def funcoes_lambda():
    # LAMBDA É COMO SE FOSSE UMA FUNÇÃO ANÔNIMA(FUNÇÃO SEM NOME), SENDO MUITO ÚTIL QUANDO PRECISAMOS CRIAR FUNÇÕES CURTAS E SIMPLES

    # FUNÇÃO NORMAL
    def soma(x, y):
        return x + y

    print(soma(2, 3))

    # FUNÇÃO LAMBDA:
    soma = lambda x, y: x + y
    print(soma(2, 3)) 



# EU NÃO PRECISO OBRIGATORIAMENTE ESPECIFICAR O TIPO DE EXCEÇÃO EM PYTHON PORÉM ISSO VAI DIFICULTAR O DEBUG.
def usando_excecoes():
    try:
        numero = int (input("DIGITE UM  NÚMERO?"))
        print(numero)
    except:
        print("Você não digitou um número")
    finally:
        print("Programa finalizado!")

def main():
    funcoes_lambda()
main()
