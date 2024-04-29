"""
Ruben Blas Lario, Iker Blazquez Valverde
22/01/2024 - M03 UF1 Pr5

e2. Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.

Per aconseguir nombres aleatoris en Python podem utilitzar la funció random.randint(limitInferior,limitSuperior)
# Program to generate a random number between 0 and 9
# importing the random module
import random
print(random.randint(0,9))

Reconocimiento: Numero Aleatorio de 1 a 50 > Crear Lista de 100 > Pares y Impares > Mediana

Utilidad: Calcular la media de pares e impares de una lista de numero aleatorios
"""
import random
#Numero Aleatorio de 1 a 50: "random.randint(1,50)"
#Crear Lista de 100: "[... for i in range(100)]"
Lista = [random.randint(1,50) for i in range(100)]
#Pares y impares: "Lista[0::2]" y "Lista[1::2]"
#Mediana: sum(...) / len(...)
medPar, medImpar = sum(Lista[0::2]) / len(Lista[0::2]), sum(Lista[1::2]) / len(Lista[1::2])
print("Pares: " + str(medPar) + "\nImpares: " + str(medImpar))
