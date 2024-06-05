"""

   Oriol Barba Vázquez
   04/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -HowBigIsYourPizza
    Llegeix el diametre d'una pizza rodona i imprimeix la seva superfície. Pots usar Math.PI per escriure el valor de Pi.

"""
import math

diametrePizza = float(input("Escriu el diametre de la pizza: "))
radiPizza = diametrePizza/2

areaPizza = math.pi *(radiPizza ** 2)
areaPizza = round(areaPizza,2)
print(areaPizza)