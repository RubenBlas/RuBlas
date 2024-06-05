"""
   Oriol Barba Vázquez
   13/12/2022
   ASIXc M03 UF1 PP2
   Descripció: Estructures de Repeticio
   MatrixDiagonals
"""
# Dos bucles que controlan las filas i cada numero de la Matriz
for i in range(8):
    for j in range(8):
        if i == j:
            print("1",end="  ")
        elif i+j == 7:
            print("2",end="  ")
        else:
            print("0",end="  ")
    print("")