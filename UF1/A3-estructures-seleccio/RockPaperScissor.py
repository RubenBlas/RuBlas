"""

   Oriol Barba Vázquez
   03/10/2022
   ASIXc M03 UF1 A3

    Descripció: RockPaperScissors

    Volem fer el joc de pedra, paper, tisora.

L'usuari introdueix dos enters (1) pedra, (2) paper, (3) tisora.

Imprimeix per pantalla Guanya el primer, Guanya el segon, Empat segons els enters introduïts.

Input

1 2

Output

Guanya el segon

"""

print("Jugarem un Joc, Rock, Paper, Scissors!")
print("Les regles son les següents: pedra (1) - paper (2) - tisora (3)")
primerNumero = int(input("Introdueix un del tres numeros: "))
segonNumero = int(input("Introdueix un del tres numeros: "))

if (primerNumero == 1 or primerNumero == 2 or primerNumero == 3) and (segonNumero == 1 or segonNumero == 2 or segonNumero == 3):

    if (primerNumero == 1 and segonNumero == 1) or (primerNumero == 2 and segonNumero == 2) or (primerNumero == 3 and segonNumero == 3):
        print("Empat!")
    elif primerNumero == 1 and segonNumero == 2:
        print("Guanya el segon Jugador!")
    elif primerNumero == 1 and segonNumero == 3:
        print("Guanya el primer Jugador!")
    elif primerNumero == 2 and segonNumero == 1:
        print("Guanya el primer Jugador!")
    elif primerNumero == 2 and segonNumero == 3:
        print("Guanya el segon Jugador!")
    elif primerNumero == 3 and segonNumero == 1:
        print("Guanya el segon Jugador!")
    elif primerNumero == 3 and segonNumero == 2:
        print("Guanya el primer Jugador!")

else:
    print("numero fora del rang")