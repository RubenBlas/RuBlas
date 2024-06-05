"""

   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -InRange

InRange
Escriu un programa que llegeixi 5 enters. El primer i el segon creen un rang, el tercer i el quart creen un altre rang.
Mostra true si el cinquè valor està en els dos rangs, sino false.
"""

# Llegeix els 5 enters
primerNumero = int(input("Escriu el primer numero enter: "))
segonNumero = int(input("Escriu el segon numero enter: "))
tercerNumero = int(input("Escriu el tercer numero enter: "))
quartNumero = int(input("Escriu el cuart numero enter: "))
cinqueNumero = int(input("Escriu el cinqué numero enter: "))

# Interpreta els 2 rangs i fa la impressió de true o false
print(bool(primerNumero <= cinqueNumero <= segonNumero))
print(bool(tercerNumero <= cinqueNumero <= quartNumero))

