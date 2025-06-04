from utils import *

### 9. Calculadora de Fatorial

# Peça um número e calcule seu fatorial usando laços (`for` ou `while`).

def main():
    num = input_int("Informe o valor de num: ")
    print(fatorial(num))


if __name__ == "__main__":
    main()