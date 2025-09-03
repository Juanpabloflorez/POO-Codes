#Autor: Juan Pablo Florez Rubio

RespuestasNombre=[None]*6
RespuestasCarrera=[None]*6
RespuestasIdea=[None]*6


for i in range(6):
    print("Persona ", i+1)
    RespuestasNombre[i] = str(input("Ingrese su nombre: "))
    RespuestasCarrera[i] = str(input("Ingrese su carrera: "))
    RespuestasIdea[i] = str(input("Ingrese su idea de proyecto: "))
    print("\n")

print("RESULTADOS")
print("\n")
for i in range(6):
    print("Persona ", i+1)
    print("Nombre: ", RespuestasNombre[i])
    print("Carrera: ", RespuestasCarrera[i])
    print("Idea de proyecto: ", RespuestasIdea[i])
    print("\n")


