"""
Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
   Descripció: Estructures de Repetició
Mostrar per pantalla un quadrat de mida N (la triarà l'usuari)
Cal "printar"  #  a les vores. És a dir, dalt, baix dreta i esquerra
Cal fer servir estructures de repetició, per fer servir la mínima quantitat possible de sentències print
"""
alturaUsuari = int(input())
SIMBOL = "#"
SEPARACIO = " "
for i in range(alturaUsuari):
    for j in range(alturaUsuari+1):
        if j == 1:
            print(SIMBOL,end="")
        elif i == 0 or i == alturaUsuari-1:
            print(SIMBOL,end="")
        elif (i != 0 or i != alturaUsuari-1) and j == alturaUsuari -1:
            print((SEPARACIO * (alturaUsuari-1)) + SIMBOL, end="")
    print("")