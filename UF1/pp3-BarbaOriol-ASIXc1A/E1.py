"""
Oriol Barba Vázquez
24/01/2023
ASIXc M03 UF1 A5
"""
# Declaració de Variables
FILES = int(input())
COLUMNES = int(input())
cont = 0
# Comprovem si es quadrada
if FILES == COLUMNES:
    matriu = [[0]*COLUMNES for i in range(FILES)]
    for i in matriu:
        matriu[cont][0] = 1
        matriu[cont][COLUMNES-1] = 1
        cont += 1
        # Fem que la meitat de la matriu sigui completa de 1
        matriu[FILES//2][cont-1] = 1
    cont = 0
    # Bucle que primpta les files quan la variable 'cont' augmenta
    for t in matriu:
        print(matriu[cont])
        cont += 1
else:
    print("No es quadrada")
