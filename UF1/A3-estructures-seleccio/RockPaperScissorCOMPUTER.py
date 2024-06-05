"""

   Oriol Barba Vázquez
   03/10/2022
   ASIXc M03 UF1 A3

    Descripció: RockPaperScissors

Volem fer el joc de pedra, paper, tisora. Aquesta vegada jugant 1 usuari contra l'ORDINADOR

L'usuari introdueix només un enter:  (1) pedra, (2) paper, (3) tisora.

Imprimeix per pantalla Guanya el primer, Guanya el segon, Empat segons els enters introduïts.

Input

1

Output

l'Ordinador ha triat 2

Guanya l'ordinador

PISTA -------------------------------------------

import random
aleatori= int(random.uniform(1, 3))
"""
import random

print("Jugarem un Joc, Rock, Paper, Scissors!")
print("Les regles son les següents: pedra (1) - paper (2) - tisora (3)")
primerNumero = int(input("Introdueix un del tres numeros: "))
aleatorio = int(random.uniform(1,3))
if (primerNumero == 1 or primerNumero == 2 or primerNumero == 3) and (aleatorio == 1 or aleatorio == 2 or aleatorio == 3):

    if (primerNumero == 1 and aleatorio == 1) or (primerNumero == 2 and aleatorio == 2) or (primerNumero == 3 and aleatorio == 3):
        print("Empat!")
    elif primerNumero == 1 and aleatorio == 2:
        print("Guanya el ordinador!")
    elif primerNumero == 1 and aleatorio == 3:
        print("Guanya el Jugador!")
    elif primerNumero == 2 and aleatorio == 1:
        print("Guanya el Jugador!")
    elif primerNumero == 2 and aleatorio == 3:
        print("Guanya el ordinador!")
    elif primerNumero == 3 and aleatorio == 1:
        print("Guanya el ordinador!")
    elif primerNumero == 3 and aleatorio == 2:
        print("Guanya el Jugador!")

else:
    print("numero fora del rang")