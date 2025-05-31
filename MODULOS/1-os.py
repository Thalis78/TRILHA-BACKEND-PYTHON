import os

# MODULO OS É USADO PARA INTERAGIR COM O SISTEMA OPERACIONAL COMO UM TODO, INCLUINDO MANIPULAÇÃO DE ARQUIVOS, DIRETÓRIOS E VÁRIAVEIS DE AMBIENTE.

# RETORNAR ARQUIVOS E PASTAS
print(os.getcwd())

# LISTAR ARQUIVOS E PASTAS
print(os.listdir())

# VERSÃO DE SO
os.system("ver")

# CONFIGURAÇÕES DA MÁQUINA
os.system("systeminfor")

# LIMPAR A TELA DO TERMINAL
os.system("cls")

# DESLIGAR O COMPUTADOR
os.system('shutdown /s /t 0')

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')
