#Autor: Juan Pablo Florez Rubio

class perro:
    def __init__(self, sonido):
        self.sonido = sonido

sonido=str(input("¿Como suena el perro?: "))
unperro=perro(sonido)

class gato:
    def __init__(self, sonido):
        self.sonido = sonido

sonido=str(input("¿Como suena el gato?: "))
ungato=gato(sonido)

print("El perro hace ",unperro.sonido)
print("El gato hace ",ungato.sonido)