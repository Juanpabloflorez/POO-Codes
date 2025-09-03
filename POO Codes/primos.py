#Autor: Juan Pablo Florez Rubio

min = 1
max = 50

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

for numero in range(min, max):
    if primo(numero)==True:
        print(numero)