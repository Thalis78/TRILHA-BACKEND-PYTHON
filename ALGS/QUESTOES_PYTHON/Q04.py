from utils import *

### 4. Verificador de Palíndromo

# Verifique se a palavra digitada pelo usuário é um palíndromo (ex: “radar”, “arara”).

def palindromo(caractere):
    if(eh_palindromo(caractere)):
        print("É palíndromo!")
    else:
        print("Não é palíndromo.")

def main():
    caracter_usuario = input_string("Digite uma palavra: ")
    palindromo(caracter_usuario)

if __name__ == "__main__":
    main()
