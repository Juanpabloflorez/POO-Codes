#Autor: Juan Pablo Florez Rubio
#Primera version

#1. Estructuras de control
#if, for, while, switch, dowhile

#Prueba
# Estructure un programa que mencione si su calificacion es meritoria
#4.5 a 5 es meritorio

nota = float(input("Ingrese la nota en forma numerica entre 0 y 5: "))

if(nota>=4.5):
    print("Esta nota es meritoria")
else:
    print("Esta nota no es meritoria")


#Ejercicio 12
print("\n")
print("Ejercicio 12")
contador=5
while(contador<16):
    print(contador," ")
    contador=contador+1

#Ejercicio 14

print("\n")
print("Ejercicio 14")
for i in range(1, 201):
    print("hola")

#Ejercicio 16

mult=1
for i in range(1,21):
    mult=mult*i
print("\n")
print("Ejercicio 16")
print("La multiplicacion de los primeros 20 numeros naturales es: ",mult)

#Ejercicio 21
print("\n")
print("Ejercicio 21")
uno = float(input("Ingrese un numero: "))
dos = float(input("Ingrese otro numero: "))
if(uno>dos):
    print(uno,">",dos)
else:
    print(uno,"<",dos)