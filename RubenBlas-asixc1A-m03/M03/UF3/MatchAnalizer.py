#insert nom1 y nom2 + sus victorias, crear un def que printe los diferentes casos en funcion a los parametros de gol
equipo1 = "Equipo1" #input("Equipo1 ")
equipo2 = "Equipo2" #input("Equipo2 ")
puntuacion = "0 0"
def contador(nuevapuntuacion):
    if int((nuevapuntuacion.split(" ")[0])) > int(puntuacion.split(" ")[0]):
        if (int((nuevapuntuacion.split(" ")[0])) - int(puntuacion.split(" ")[0])) == 1:
            print("Tiro libre de " + equipo1)
        elif (int((nuevapuntuacion.split(" ")[0])) - int(puntuacion.split(" ")[0])) == 2:
            print("Canasta de " + equipo1)
        elif (int((nuevapuntuacion.split(" ")[0])) - int(puntuacion.split(" ")[0])) == 3:
            print("Triple " + equipo1)
    elif int((nuevapuntuacion.split(" ")[1])) > int(puntuacion.split(" ")[1]):
        if (int((nuevapuntuacion.split(" ")[1])) - int(puntuacion.split(" ")[1])) == 1:
            print("Tiro libre de " + equipo2)
        elif (int((nuevapuntuacion.split(" ")[1])) - int(puntuacion.split(" ")[1])) == 2:
            print("Canasta de " + equipo2)
        elif (int((nuevapuntuacion.split(" ")[1])) - int(puntuacion.split(" ")[1])) == 3:
            print("Triple de " + equipo2)


while contador != "-1":
    nuevapuntuacion = input()
    contador(nuevapuntuacion)
    puntuacion = nuevapuntuacion
"""
    print(str(goles1) + " " + str(goles2))

while goles != "-1";
comentador(input())
"""


#Quien de los dos marca
#Tipos de tiros: Tiro libre, Canasta y Triple
