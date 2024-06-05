"""
Exercici 1
S'ha creat un nou embàs, amb forma de piràmide quadrangular, per omplir-la
 d'aliments. Com ara: gelats, xocolates, o qualsevol altre aliment cremós
Ens demanen, crear un programa que mostri per pantalla, l’àrea i el volum
d’una piràmide quadrangular (de base quadrada) on l'alçada i la mida dels
 costats es llegeix del teclat. Les fórmules són les que es mostren a la
 imatge.

"""

import math

# Creem les variables que haurà de omplir l'usuari
llargariaCostat = float(input("Introduiex el valor del costat de la base del triangle rectangular: "))
alturaCostat = float(input("Introdueix el valor de la alçada del triangle rectangular: "))

# Calculem el valor de l'Area i el volum del triangle
areaTriangle = llargariaCostat * (llargariaCostat + math.sqrt((4 * pow(alturaCostat, 2)) + pow(llargariaCostat, 2)))
volumTriangle = (pow(llargariaCostat, 2) * alturaCostat)/3

# Imprimim els valors per la consola
print("Area = ", round(areaTriangle, 2), "metres quadrats")
print("Volum = ", round(volumTriangle, 2), "metres cúbics")
