# main.py
from diferencia import desordenar_texto

texto = "Ejemplo123@Python!"
caracteres_alfabeticos = []
caracteres_especiales = []

contador_alfabeticos = 0
contador_especiales = 0


# Llamada a la función principal
caracteres_alfabeticos, caracteres_especiales, texto_desordenado = desordenar_texto("Ejemplo123@Python!")

# Imprimir resultados
print(caracteres_alfabeticos)
print(caracteres_especiales)
print(texto_desordenado)
