"""
L'usuari introdueix una hora amb tres enters (hores, minuts i segons).
Imprimeix l'hora que serà al cap d'un segon

Input
10 50 59
Output
12:51:00
"""

usuariHora = str(input("Introdueix hora minuts i segons: "))

x = usuariHora.split(" ")

segundos = x[2]
minutos = x[1]
horas = x[0]

segundos = int(segundos) + 1
segundos = str(segundos)

if segundos == "60":

    segundos = "00"

    minutos = int(minutos) + 1
    minutos = str(minutos)


if minutos == "60":

    minutos = "00"

    horas = int(horas) + 1
    horas = str(horas)

print(horas, end=":")
print(minutos, end=":")
print(segundos)


