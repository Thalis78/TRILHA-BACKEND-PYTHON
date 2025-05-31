import random

#SELECIONAR VALOR ALEATÓRIO DE UMA LISTA
list1 = [7,6,4,3,2,1]
print(random.choice(list1))

# GERA UM NÚMERO ALEATÓRIO EM UM INTERVALO DE VALORES
r1 = random.randint(5,15)
print(r1)

# SELECIONA CARACTERE ALEATÓRIO DE UMA STRING
name = "CURSO PYTHON"
r2 = random.choice(name)
print(r2)

# SELECIONA MAIS DE UM VALOR ALEATÓRIO
print(random.sample(name,2))

# PROGRAMA DE SORTEIO
done = False
while not done:
    print("O que você deseja fazer?")
    print("1. Adivinhar o número")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print("===================Adivinhe um número de 1 a 10:====================\n")
        number = int(input("NUMERO(1 A 10): "))
        result = random.randint(1,10)

        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f"Tente novamente. O número era {result}")
    elif choice == "2":
        print("PROGRAMA FINALIZADO!") 
        done = True
    else:
        print("Opção inválida. Escolha a opção 1 ou 2.")   