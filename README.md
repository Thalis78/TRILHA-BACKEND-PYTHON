# Trilha Backend Django - Revisão Geral

Este repositório acompanha a trilha de estudos em backend com Django, onde revisamos conceitos fundamentais de lógica de programação, módulos, Programação Orientada a Objetos (POO) e a arquitetura do Django, incluindo MVT e uso de REST API.

---

## 1. Revisão de Lógica de Programação

- Estruturas básicas: variáveis, condicionais e loops
- Fluxo de controle
- Tipos de dados e operadores
- Resolução de problemas e algoritmos simples

---

## 2. Revisão de Módulos em Python

- Importação e organização de código
- Uso de bibliotecas padrão e externas
- Modularização para reaproveitamento e manutenção

---

## 3. Programação Orientada a Objetos (POO)

- Classes e objetos
- Encapsulamento, herança e polimorfismo
- Métodos e atributos
- Abstração e composição

---

## 4. Tratamento de Exceções em Python

### 4.1 Conceito

Exceções são eventos que ocorrem durante a execução do programa e que interrompem seu fluxo normal. O tratamento de exceções permite lidar com erros de forma segura, evitando que o programa quebre inesperadamente.

### 4.2 Sintaxe básica

```
python:

try:
    resultado = int("abc")
except ValueError:
    print("Erro: valor inválido para conversão.")
```

---

## 5. Arquitetura Django: MVT vs REST API

### 5.1 Arquitetura MVT no Django

- **MVT**: Model - View - Template
- Estrutura padrão do Django para aplicações web monolíticas.
- **Model**: Representa dados e regras de negócio.
- **View**: Processa requisições, acessa dados e retorna resposta.
- **Template**: Gera o HTML que será exibido no cliente.

### 5.2 Uso da arquitetura MVT

- Ideal para aplicações monolíticas, onde front e back-end estão juntos.
- A View gera as páginas HTML diretamente.

### 5.3 Separação entre front-end e back-end

- Quando front e back são separados, o back funciona como uma REST API.
- O back envia dados (JSON) e o front consome e renderiza a interface.
- Django pode atuar apenas como API backend (exemplo: com Django REST Framework).

### 5.4 Resumo

| Arquitetura | Uso típico                      | Front-end                 | Back-end                    |
| ----------- | ------------------------------- | ------------------------- | --------------------------- |
| MVT         | Aplicações monolíticas          | Templates Django (HTML)   | Lógica e dados no Django    |
| REST API    | Sistemas com front-end separado | Framework JS (React, Vue) | API REST no Django ou outra |

---
