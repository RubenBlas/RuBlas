"""
   Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
   Descripció: Estructures de Repetició

S'imprimeix una piràmide d'altura N de #
"""
altura = int(input("Introdueix l'altura de la piramide: "))
SIMBOL = "#"
for i in range(altura):
    print(SIMBOL)
    SIMBOL += "#"
