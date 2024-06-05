"""

   Oriol Barba Vázquez
   04/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -CalculateDiscount
    Llegeix el preu original i el preu actual i imprimeix el descompte (en %).

"""
#Asigant les variables
preuOriginal = float(input("Escriu el preu original: "))
preuActual = float(input("Escriu el preu actual: "))

#Formula del Descompte
descompte = 100-((preuActual*100)/preuOriginal)
descompte = round(descompte,2)

#Imprimint el resultat
print("El teu descompte es: "+str(descompte)+"%")

