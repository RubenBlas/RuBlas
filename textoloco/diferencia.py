# diferencia.py
from desordenar import desordenar_secuencia
def desordenar_texto(texto):
    caracteres_alfabeticos = []
    caracteres_especiales = []

    contador_alfabeticos = 0
    contador_especiales = 0

    for i in range(len(texto)):
        if texto[i].isalpha():
            caracteres_alfabeticos.append(texto[i])
            caracteres_especiales.append("")
            contador_alfabeticos += 1
            contador_especiales = 0  # Reiniciar contador de caracteres especiales
        else:
            if contador_especiales == 0 and contador_alfabeticos > 3:
                desordenar_secuencia(caracteres_alfabeticos, i - contador_alfabeticos, i)

            caracteres_alfabeticos.append("")
            caracteres_especiales.append(texto[i])
            contador_especiales += 1
            contador_alfabeticos = 0  # Reiniciar contador de caracteres alfabéticos

    # Unir las listas y obtener el texto desordenado
    texto_desordenado = ''.join([a + b for a, b in zip(caracteres_alfabeticos, caracteres_especiales)])

    return caracteres_alfabeticos, caracteres_especiales, texto_desordenado