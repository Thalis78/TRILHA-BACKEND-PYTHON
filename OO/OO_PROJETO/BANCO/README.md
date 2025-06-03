# Sistema de Conta Bancária - Projeto Orientado a Objetos em Python

Este projeto é um exemplo simples de Orientação a Objetos (OO) em Python, que simula um sistema básico de contas bancárias.

---

## Funcionalidades

- Criar contas com titular e saldo inicial
- Depositar valores na conta
- Sacar valores da conta, com verificação de saldo
- Transferir valores entre contas
- Consultar saldo da conta

---

## Estrutura do Projeto

- `Conta`: classe que representa uma conta bancária, com métodos para depósito, saque, transferência e consulta de saldo.

---

## Exemplo de Uso

```python
conta1 = Conta("Alice", 1000)
conta2 = Conta("Bob", 500)

conta1.depositar(200)
conta1.sacar(150)
conta1.transferir(300, conta2)

print(conta1.consultar_saldo())  # Deve mostrar 750
print(conta2.consultar_saldo())  # Deve mostrar 800
```
