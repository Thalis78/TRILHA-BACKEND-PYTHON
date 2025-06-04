from utils import *

### 3. Contador de Vogais
# Solicite uma frase e conte quantas vogais (`a`, `e`, `i`, `o`, `u`) ela contém, desconsiderando maiúsculas/minúsculas.

def main():
    caractere = input_string("Informe uma frase : ")
    count = contar_vogais_existente(caractere)
    print(f"Quantidade de vogais presente: {count}")
if __name__ == "__main__":
    main()