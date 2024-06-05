"""
L'usuari introdueix una hora amb tres enters (hores, minuts i segons).
Imprimeix l'hora que serà al cap d'un segon

Input
10 50 59
Output
10:51:00

EXTRA BONUS:

Mostrar l'hora sistema, en comptes de demanar-li a l'usuari.

Demanar en quants segons es vol incrementar l'hora, i mostrar per pantalla "quina seria" l'hora (No es demana modificar
l'hora del sistema)
"""
import datetime

hora = datetime.datetime.now()
horaActual = hora.strftime("%H %M %S")
x = horaActual.split(" ")


segundos = int(x[2])
minutos = int(x[1])
horas = int(x[0])

print(horaActual)
SumaSegonsUsuari = int(input("Quants segons vols sumar? "))
segundos = segundos + SumaSegonsUsuari

if segundos >= 60:

    divisio = segundos // 60
    segundos = segundos - (divisio * 60)
    minutos = minutos + divisio

if minutos >= 60:

    divisioMin = minutos // 60
    minutos = minutos - (divisioMin * 60)
    horas = horas + divisioMin

#Poso el While perque quan torna a mes de 24 hores torni a restar fins arribar a l'hora correcte
while horas >= 24:

    divisioHoras = horas // 24
    horas = horas - (divisioHoras * 24)
    horas = horas + (divisioHoras - 1)

print(horas, end=":")
print(minutos, end=":")
print(segundos)


