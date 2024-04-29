"""
Gerard Cano Maneja Oriol Barba Ruben Blas
15/2/2023
ASIXc M03 UF2
Descripció: R1:Disseny descendent i dividir en funcions
"""
from random import sample
from string import digits,punctuation
# demanem la frase per prompt
DIGITOS = digits
SIGNOS = punctuation

def demanar_frase():
    frase = input("")
    return frase
# separar la frase amb un split
def separar_frase(frase):
    frase_separada = frase.split(" ")
    return frase_separada
# fem un 'for' que recorre totes les paraules de la frase
def recorrer_frase(lista_frase):
    lista_palabras_mod = []
    for palabra in lista_frase:
        palabra_separada = list(palabra)
        palabra_partida = palabra_separada[1:-1]
        palabra_desordenada = ''.join(sample(palabra_partida,len(palabra_partida)))
        lista_palabras_mod.append(palabra_separada[0]+palabra_desordenada+palabra_separada[-1])

    print(' '.join(lista_palabras_mod))
             
prompt_frase = demanar_frase()
frase_separada = separar_frase(prompt_frase)
recorrer_frase(frase_separada)
