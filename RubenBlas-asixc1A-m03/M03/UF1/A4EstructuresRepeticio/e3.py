"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e3. Programa que mostra per pantalla la suma de tots els nombres senars i de tots
els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
 Ex: 	ssi el límit é 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729

Reconocimiento: Insertar numero limite > Suma pares  > Suma senares > Imprime sumas pares y senares




#Imprime sumas pares y senares


Utilidad: INPUT(Insertar numero limite) > OUTPUT(Imprime sumas pares y senares)
"""
sumaP=0
sumaI=0
try:
    limit = int(input())
    LIMITF = limit
    while limit != 0:
        # Suma pares
        if limit % 2 == 0:
            sumaP = sumaP + limit
            limit = limit - 1
        # Suma senares
        else:
            sumaI = sumaI + limit
            limit = limit - 1
    # Insertar numero limite
    print("Si el límit és", LIMITF, "la suma de parells es", sumaP, " i la suma de senars és ", sumaI)

except ValueError:
        print("Datos invalidos")


