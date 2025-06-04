from utils import *

### 10. Cadastro de Pessoas

# Cadastre o nome e idade de 3 pessoas, armazenando os dados em uma lista de dicionários. Mostre:

# - A pessoa mais velha
# - A média das idades

# ---

def quantidade_pessoas_que_serao_cadastrada(quantidade):
    pessoas = []
    for i in range(quantidade):
        nome = input_string("INFORME SEU NOME: ")
        idade = input_int("INFORME SUA IDADE: ")
        pessoas.append(cadastrar_pessoa(nome,idade))

    return pessoas

def pessoa_mais_velha(pessoa):
    nome = ""
    idade = 0
    for i in pessoa:
        if idade < i['year']:
            idade = i["year"]
            nome = i['name']

    return nome

def media_idades(pessoa):
    media = 0
    for i in pessoa:
        media += i["year"]
    
    return media / (len(pessoa))

def cadastrar_pessoa(nome,idade):
    return {
        "name" : nome,
        "year": idade
    }

def main():
    lista_pessoa = quantidade_pessoas_que_serao_cadastrada(3)
    nome_pessoa_mais_velha = pessoa_mais_velha(lista_pessoa)
    media_idade = arredondar_pra_baixo(media_idades(lista_pessoa))
    print(
        f"\nPESSOA MAIS VELHA: {nome_pessoa_mais_velha}"
        f"\nMEDIA IDADADE    : {media_idade}")

if __name__ == "__main__":
    main()