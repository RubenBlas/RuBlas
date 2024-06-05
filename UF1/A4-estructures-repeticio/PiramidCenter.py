"""
   Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
   Descripció: Estructures de Repetició

S'imprimeix una piràmide d'altura N de #
"""
altura = int(input("Introdueix l'altura de la piramide: "))

for i in range(altura):
    espacio = altura - i - 1
    simbolos = i * 2 + 1
    print("  " * espacio + "🧱" * simbolos)




