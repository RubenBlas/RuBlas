"""
Oriol Barba Vázquez
   10/01/2023
   ASIXc M03 UF1 A5

L’objectiu d’aquest exercici és crear un programa que utilitzi un diccionari per calcular el DNI.
A la Web del Ministerio del Interior es pot trobar l’explicació de com fer-ho.
Els passos a seguir, bàsicament són:
Es divideix el nombre entre 23 i la resta se substitueix per una lletra que es determina per inspecció mitjançant la
següent taula:
"""
try:
    dniUsuari = int(input())
    resultat = dniUsuari%23
    lista = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    print(lista[resultat])
except:
    print("ERROR")
