"""

   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -HowBigIsYourPizza
    Llegeix el diametre d'una pizza rodona i imprimeix la seva superfície. Pots usar Math.PI per escriure el valor de Pi.

"""

#importem la llibreria "math"
import math

diametrePizza = float(input("Escriu el diametre de la pizza: "))
radiPizza = diametrePizza/2

#Formula del cercle de la pizza
areaPizza = math.pi *(radiPizza ** 2)
areaPizza = round(areaPizza,2)

#Imprimir el valor de la superficie de la pizza
print(areaPizza)