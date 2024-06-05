"""
Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
Fer un programa que dibuixa un avet del Canadà.
Cal demanar la mida de l'arbre. La mida inclou el tronc i les branques
"""
TRONC = "🪵"
BOLES = "🔴"
FULLES = "🌿"
ESTEL = "🔸"
ESPACIO = "  "
alturaArbre = int(input())
alturaEstel = int(alturaArbre * 0.75)
alturaTronc = int(alturaArbre * 0.25)
alturaFulles = int(alturaArbre * 0.50)
contador = 1

for i in range(alturaArbre):
    for j in range(alturaArbre):
        # Construim el tronc de l'arbre
        if alturaArbre >= i >= alturaArbre - alturaTronc and j == alturaArbre//2:
            print((ESPACIO * (alturaArbre//2)) + TRONC,end="")
        # Construin la estructura de l'arbre
        if alturaEstel <= i < alturaArbre - alturaTronc:
            espaiFulles = alturaFulles - j - 1
            print(espaiFulles * FULLES,end="")

    print("")

