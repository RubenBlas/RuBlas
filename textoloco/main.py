# main.py
from ordenar import ordenar_texto
from texto import in_texto, out_texto


caracteres_alfabeticos = []
caracteres_especiales = []

contador_alfabeticos = 0
contador_especiales = 0


# Llamada a la función principal
caracteres_alfabeticos, caracteres_especiales, texto_desordenado = ordenar_texto(in_texto)
out_texto(ordenar_texto)

# Imprimir resultados
print(caracteres_alfabeticos)
print(caracteres_especiales)
print(texto_desordenado)
