from random import sample

def getCrazy(entrada):
    frase_separada = entrada.split(" ")
    lista_palabras_mod = []
    for palabra in frase_separada:
        palabra_separada = list(palabra)
        palabra_partida = palabra_separada[1:-1]
        palabra_desordenada = ''.join(sample(palabra_partida,len(palabra_partida)))
        lista_palabras_mod.append(palabra_separada[0]+palabra_desordenada+palabra_separada[-1])
    print(' '.join(lista_palabras_mod))