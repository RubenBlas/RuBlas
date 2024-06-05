"""
   Oriol Barba Vázquez
   13/12/2022
   ASIXc M03 UF1 PP2
   Descripció: Estructures de Repeticio
   My Replace
"""
# Creamos las variables para subistituir la frase
fraseUsuari = input()
caracter = input()
caracterSubstitucio = input()
# Un bucle para comprovar cada letra
for i in fraseUsuari:
      nuevaFrase = fraseUsuari.replace(caracter,caracterSubstitucio)
print(nuevaFrase)
