"""

   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -EOP 2
   Expliqueu que passa a:
adn = "ATGAACTGTGC"
adn=adn.replace('A', 'a')
adn=adn.replace('T', 'A')
adn=adn.replace('a', 'T')

"""

#Guardem un string en la variable "adn"
adn = "ATGAACTGTGC"

"""
El que passa aqui es que les A es canvien per les a.
Despres les T es canvien per les A.
Y finalment les a es canvien per les T.

Donant lloc a un canvi en la paraula "adn"
"""
adn = adn.replace("A", "a")
adn = adn.replace("T","A")
adn = adn.replace("a","T")

print(adn)