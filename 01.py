# 1. Comprimento da string   
# Escreva uma função que receba uma string e retorne o número de caracteres (incluindo 
# espaços).   
# Exemplo: `"Olá mundo"` → `9` 

def comprimento_string(s):
    return len(s)

s = input("digite: ")
print(comprimento_string(s))
