from utils import *

### 2. Contagem Regressiva
# Receba um número `n` e faça uma contagem regressiva até zero, com 1 segundo de intervalo entre os números.

def regressiva(numero):
    for i in range(numero,-1,-1):
        intervalo(1)
        print(i)

def main():
    numero_usuario = input_int("Informe o número para usar na regressiva: ")
    regressiva(numero_usuario)

if __name__ ==  "__main__":
    main()