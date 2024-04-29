equipos = ("Equipo1", "Equipo2") #str(input("Inscribe al equipo local")) #str(input("Inscribe al equipo visitante"))
puntuacion = "0 0"
tiro = ("XD", "Tiro libre", "Canasta", "Triple")
def contador(nuevapuntuacion):
    if int((nuevapuntuacion.split(" ")[0])) > int(puntuacion.split(" ")[0]):
        equipo = 0
    elif int((nuevapuntuacion.split(" ")[1])) > int(puntuacion.split(" ")[1]):
        equipo = 1
    diferencia = (int((nuevapuntuacion.split(" ")[equipo])) - int(puntuacion.split(" ")[equipo]))
    print(tiro[diferencia] + " de " + equipos[equipo])
while contador != "-1":
    nuevapuntuacion = input()
    contador(nuevapuntuacion)
    puntuacion = nuevapuntuacion