from models.conta import *

def main():
    conta1 = Conta("Alice", 1000)
    conta2 = Conta("Bob", 500)

    conta1.depositar(200)
    conta1.sacar(150)
    conta1.transferir(300, conta2)

    print(conta1.consultar_saldo()) 
    print(conta2.consultar_saldo()) 

if __name__ == "__main__":
    main()