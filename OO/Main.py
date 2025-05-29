from Carro import Carro;

def main():
    carro1 = Carro("Fiat", 2020, "Argo", 50000)
    
    print(carro1.get_ano())
    print(carro1.get_nome())
    print(carro1.get_modelo())
    print(carro1.get_valor())

    carro1.set_modelo("UNO")
    carro1.set_valor(42000)

    print()
    print(carro1.get_ano())
    print(carro1.get_nome())
    print(carro1.get_modelo())
    print(carro1.get_valor())


main()
