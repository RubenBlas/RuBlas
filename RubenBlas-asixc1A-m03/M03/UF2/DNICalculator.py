"""
Rubén Blas Lario
18/10/2022
ASIXc M03 UF1 A3
Descripció: EsAnyDeTraspas
El programa ha de mostrar un dels dos missatges possibles,
 que són Any de traspàs o Any comú, segons el valor ingressat.
 (Només llegir el número d'any, per facilitar l'algoritme)
"""
try:
    DNI = int(input("Inserta los numeros de tu DNI "))
    if len(str(DNI)) == 8:
        traductor = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        print(traductor[(int(DNI % 23))])
except:
    print("Ni el DNI te sabes")