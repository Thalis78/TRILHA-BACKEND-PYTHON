from utils import *

# ### 8. Inversão de String

# Peça uma palavra e a exiba invertida (sem usar `[::-1]`).

def main():
    palavra = input_string("Palavra: ")
    print(inverter_string(palavra))

if __name__ == "__main__":
    main()