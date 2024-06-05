"""
   Oriol Barba Vázquez
   03/10/2022
   ASIXc M03 UF1 A3
   Descripció:

   Estructures de Selecció

 Com segurament sabràs, a causa d'algunes raons astronòmiques, l'any poden ser de traspàs o comú. Els primers tenen
una durada de 366 dies, mentre que els últims tenen una durada de 365 dies.
Des de la introducció del calendari gregorià (en 1582), s'utilitza la següent regla per a determinar el tipus d'any:
Si el número de l'any no és divisible entre quatre, és un any comú.
En cas contrari, si el número de l'any no és divisible entre 100, és un any de traspàs.
En cas contrari, si el número de l'any no és divisible entre 400, és un any comú.
En cas contrari, és un any de traspàs. """

numeroAño = int(input("Escribe un año: "))

if numeroAño < 1582:
    print("Data anterior a gregori")
else:
    if numeroAño % 4 != 0:
        print("Any comú")
    elif numeroAño % 100 != 0:
        print("Any de traspàs")
    elif numeroAño % 400 != 0:
        print("Any comú")
    else:
        print("Any de traspàs")
