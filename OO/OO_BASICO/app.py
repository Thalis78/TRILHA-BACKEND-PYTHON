from Carro import Carro
from CarroEletrico import CarroEletrico

def main():
    carro1 = Carro("Fiat", 2020, "Argo", 50000)

    print(carro1.ano)
    print(carro1.nome)
    print(carro1.modelo)

    carro1.modelo = "UNO"
    carro1.valor = 42000

    print()
    print(carro1.ano)
    print(carro1.nome)
    print(carro1.modelo)
    print(carro1.valor)

    tesla = CarroEletrico("Tesla", 2023, "Model 3", 280000, 500)
    print()
    print(tesla.exibir_detalhes())

if __name__ == "__main__":
    main() 
