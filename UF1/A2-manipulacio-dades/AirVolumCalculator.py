"""

   Oriol Barba Vázquez
   04/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -AirVolumeCalculator
    Per poder fer un estudi de la ventilació d'una aula necessitem poder calcular la quantitat d'aire que hi cap en una habitació. Llegeix les 3 dimencions de l'aula i printa per pantalla quin volum té.
"""

#Valor X
llargariaAula = float(input("Quina llargaria té la classe: "))

#Valor Y
alçadaAula = float(input("Quina alçada té la classe: "))

#Valor Z
ampladaAula = float(input("Quina amplada té la classe: "))

areaAula = llargariaAula * ampladaAula

volumAula = areaAula * alçadaAula

print(volumAula)