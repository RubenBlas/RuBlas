import random

def desordenar_secuencia(alfabeticos, inicio, fin):
    alfabeticos_a_desordenar = alfabeticos[inicio + 1 : fin - 1]
    random.shuffle(alfabeticos_a_desordenar)
    alfabeticos[inicio + 1 : fin - 1] = alfabeticos_a_desordenar



def desordenar_texto(texto):
    caracteres_alfabeticos = []
    caracteres_especiales = []

    contador_alfabeticos = 0
    contador_especiales = 0

    for i in range(len(texto)):
        segmentacion_texto()

    # Unir las listas y obtener el texto desordenado
    texto_desordenado = ''.join([a + b for a, b in zip(caracteres_alfabeticos, caracteres_especiales)])

    return caracteres_alfabeticos, caracteres_especiales, texto_desordenado

# Llamada a la función principal
caracteres_alfabeticos, caracteres_especiales, texto_desordenado = desordenar_texto("Ejemplo123@Python!")

# Imprimir resultados
print(caracteres_alfabeticos)
print(caracteres_especiales)
print(texto_desordenado)
