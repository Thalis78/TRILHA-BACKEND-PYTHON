import time
import random

def input_int(texto):
    try:
        return int(input(texto))
    except:
        return input_int(texto)
    
def input_float(texto):
    try:
        return float(input(texto))
    except:
        return input_float(texto)

def input_string(texto):
    try:
        return input(texto)
    except:
        return input_string(texto)

def eh_numero_par(numero):
    return numero % 2 == 0

def eh_numero_impar(numero):
    return numero % 2 != 0

def intervalo(numero):
    time.sleep(numero)

def contar_caracteres(caractere):
    count = 0
    for i in caractere:
        count+=1
    
    return count

def contar_vogais_existente(caractere):
    caractere.lower()
    count = 0
    vogais = ["a","e","i","o","u"]
    for i in caractere:
        for j in vogais:
            if(i == j):
                count+=1
                break
    return count

def eh_palindromo(caracteres):
    palindromo = ""
    for i in range(len(caracteres) -1, -1,-1):
        palindromo += caracteres[i]
    
    return palindromo == caracteres

def eh_primo(numero):
    if numero != 2 and numero != 3 and numero !=5:
        if(numero % 2 == 0):
            return
        elif(numero % 3 == 0):
            return
        elif(numero % 5 == 0):
            return
    
    return True

def fibonnaci(n):
    a = 0
    b = 1   
    soma = 0
    for i in range(n):
        if i == 0:
            print(a)
            continue
        if i == 1:
            print(b)
            continue
        soma = a + b
        a = b
        b = soma
        print(soma)

def gerar_num(num_inicial,num_final):
    return random.randint(num_inicial,num_final)

def fatorial(num):
    f = 1
    for i in range(num,0, -1):
        f *= i
    
    return f

