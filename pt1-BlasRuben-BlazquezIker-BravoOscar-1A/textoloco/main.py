# main.py
from diferencia import desordenar_texto

texto_a_marear = "Ejemplo123@Python!cmaron asdfadsf 434"
caracteres_alfabeticos = []
caracteres_especiales = []

contador_alfabeticos = 0
contador_especiales = 0


# Llamada a la función principal
caracteres_alfabeticos, caracteres_especiales, texto_desordenado = desordenar_texto(texto_a_marear)

# Imprimir resultados
print(caracteres_alfabeticos)
print(caracteres_especiales)
print(texto_desordenado)
