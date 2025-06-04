from utils import *

### 6. Número Primo

# Solicite um número e verifique se ele é primo.

def resultado_eh_primo(numero):
    if eh_primo(numero):
        print("É primo.")
        return
    
    print("Não é primo.")

def main():
    numero = input_int("Informe um número: ")

    resultado_eh_primo(numero)

if __name__ == "__main__":
    main()