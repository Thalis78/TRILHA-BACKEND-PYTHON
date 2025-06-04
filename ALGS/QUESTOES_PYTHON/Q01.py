from utils import *

# ### 1. Par ou Ímpar
# Peça um número ao usuário e informe se ele é par ou ímpar.

def eh_par_ou_impar(numero):
    if eh_numero_par(numero):
        print(
            f"\nNúmero escolhido: {numero}\n"
            f"Esse numero é par!")
    else:
        print(
            f"\nNúmero escolhido: {numero}\n"
            f"Esse numero é impar!")
def main():
    numero_informado_pelo_usuario = input_int("Informe um número inteiro: ")
    eh_par_ou_impar(numero_informado_pelo_usuario)
if __name__ == "__main__":
    main()