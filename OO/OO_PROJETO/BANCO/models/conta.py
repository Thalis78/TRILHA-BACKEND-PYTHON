class Conta:
    def __init__(self, nome, saldo=0):
        self.__nome = nome
        self.__saldo = saldo

    def __str__(self):
        return (
            f"\n========== INFORMAÇÕES DA CONTA ==========\n"
            f"| CONTA : {self.__nome}\n"
            f"| SALDO : R${self.__saldo:.2f}"
        )

    def consultar_saldo(self):
        return f"| SALDO : R${self.__saldo:.2f}"

    def sacar(self, valor_saque):
        try:
            valor_saque = float(valor_saque)
            if valor_saque > self.__saldo:
                raise ValueError("Saldo insuficiente.")
            if valor_saque <= 0:
                raise ValueError("O valor do saque deve ser positivo.")

            self.__saldo -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        except ValueError as e:
            print(f"Erro ao sacar: {e}")

    def depositar(self, deposito):
        try:
            deposito = float(deposito)
            if deposito <= 0:
                raise ValueError("O valor do depósito deve ser positivo.")

            self.__saldo += deposito
            print(f"Depósito de R${deposito:.2f} realizado com sucesso.")
        except ValueError as e:
            print(f"Erro ao depositar: {e}")

    def transferir(self, valor_transferencia, conta_destino):
        try:
            valor_transferencia = float(valor_transferencia)
            if valor_transferencia > self.__saldo:
                raise ValueError("Saldo insuficiente.")
            if valor_transferencia <= 0:
                raise ValueError("O valor da transferência deve ser positivo.")

            self.__saldo -= valor_transferencia
            conta_destino.depositar(valor_transferencia)
            print("Transferência realizada com sucesso!")
        except ValueError as e:
            print(f"Erro ao transferir: {e}")

