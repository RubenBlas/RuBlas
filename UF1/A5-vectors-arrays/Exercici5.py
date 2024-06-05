"""
Fer un programa que inicialitza una llista que haurà de contenir 10 números de l'1 al 10
(generats de manera aleatòria), després els ordena de menor a major, i finalment mostri la llista ordenada
de números per pantalla. Pista: no cal que implementeu l’ordenació de nombres en una llista, podeu fer
 servir la funció sort que ve definida en el tipus seqüència de Python.
"""
import random

llista_numerosRandom = [random.randint(1,10) for i in range (10)]
llista_numerosRandom.sort()
print(llista_numerosRandom)