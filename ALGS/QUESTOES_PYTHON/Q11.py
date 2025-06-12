def informe_a_letras():
    letras = []
    while True:
        letra_informada = input("Informe uma letra (flag = 0): ").upper()

        if(letra_informada == "0"):
            break

        letras.append(letra_informada)
    
    return letras

def contem_letras_proibidas(letras_proibidas,palavra):
    for letra in palavra:
        for letra_proibida in letras_proibidas:
            if(letra.upper() == letra_proibida):
                return True
    
    return False

def main():
    lista_de_letras_proibidas = informe_a_letras()

    eh_proibido = contem_letras_proibidas(lista_de_letras_proibidas, "cachorro")

    if(eh_proibido):
        print("SIM")
    else:
        print("NÃO")

if __name__ == "__main__":
    main()
