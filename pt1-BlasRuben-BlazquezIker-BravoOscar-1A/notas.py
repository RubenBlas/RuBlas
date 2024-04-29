#MAIN: input de dades + procesar dades

#CRAZY_WORDS: lista de palabras > modificar cada palabra (< 3)

palabra = "word,"
letras_alfabeticas = []
caracteres_especiales = []
nuevapalabra = ""
"""
if len(text) > 3:
    text
"""




#DETECTAR SI HAY UNA COMA O OTRO CARACTER QUE NO SEA ESPACIO
for letra in palabra:
    if letra.isalpha():
        nuevapalabra += letra



for i in range(len(palabra)):
    if palabra[i].isalpha():
        letras_alfabeticas.append(palabra[i])
    else:
        letras_alfabeticas.append("")
    if not palabra[i].isalpha():
        caracteres_especiales.append(palabra[i])
    else:
        caracteres_especiales.append("")

print(letras_alfabeticas)
print(caracteres_especiales)