from utils import *

### 7. Jogo de Adivinhação

# Gere um número aleatório de 1 a 100. O usuário deve tentar adivinhar, recebendo dicas (“maior” ou “menor”).

def joguinho(numero_aleatorio):
    print("TENTE NUMERO DE 1 A 100\n")
    num = input_int("| -> NUM : ")
    if(num < numero_aleatorio):
        print(f"\n** É MAIOR **\n")
        return joguinho(numero_aleatorio)
    
    if(num > numero_aleatorio):
        print(f"\n** É MENOR **\n")
        return joguinho(numero_aleatorio)

    print("\nVOCÊ ACERTOU :) ")

def main():
    num_aleatorio = gerar_num(1,100)
    joguinho(num_aleatorio)

if __name__ == "__main__":
    main()