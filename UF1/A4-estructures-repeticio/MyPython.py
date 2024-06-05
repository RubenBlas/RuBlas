"""

   Oriol Barba Vázquez
   15/11/2022
   ASIXc M03 UF1 A4

   Descripció:

   Estructures de Repetició

   Programa per crear una Python a mida.

Cal demanar quina mida ha de tenir la serp.

tot seguit mostrar-la per pantalla.

Es valorarà el fet de que el cos faci siga sagues. Potser, la mida del cos ha de ser mínim 5

"""

import time
midaSerp = int(input("Quina mida vols que tingui la serp? "))
separacio = ""
MAXIM = True
print(separacio + "hola")
COS = "    ═(███)═"
print(len(COS))
if midaSerp >= 5:

    print("    \     /     ")
    print("     ╚⊙ ⊙╝   ")
    print(COS)

    for i in range(midaSerp):

        if len(COS) <= 15:
            separacio = " " + separacio
            COS = separacio + COS
            print(COS)

        if len(COS) <= 15:
            separacio = " " + separacio
            COS = separacio + COS
            print(COS)

    print("      ═V═")

else:
    print("Mida Incorrecta")

