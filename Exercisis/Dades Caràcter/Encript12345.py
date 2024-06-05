"""
   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -Encript12345

    Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
    Tenint en compte, que la lletra a i A és l'1 , consecutivament fins a la lletra u i U que és el 5.

"""

#Creem una variable que guardarà la paraula que volem canviar
paraula = str(input("Escriu una paraula: "))

#Aquesta variable modificarà les vocals per numeros, gracies a "replace"
paraula = paraula.replace("a","1")
paraula = paraula.replace("A","1")
paraula = paraula.replace("e","2")
paraula = paraula.replace("E","2")
paraula = paraula.replace("i","3")
paraula = paraula.replace("I","3")
paraula = paraula.replace("o","4")
paraula = paraula.replace("O","4")
paraula = paraula.replace("u","5")
paraula = paraula.replace("U","5")

print(paraula)