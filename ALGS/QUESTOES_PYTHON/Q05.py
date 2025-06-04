from utils import *

### 5. Sequência de Fibonacci

# Peça um número `n` e mostre os `n` primeiros números da sequência de Fibonacci.

def main():
    num = input_int("Digite o valor de N: ")
    print(
        f"============= FIBONACCI ================\n"
        f"Número escolhido: {num}")
    fibonnaci(num)

if __name__ == "__main__":
    main()