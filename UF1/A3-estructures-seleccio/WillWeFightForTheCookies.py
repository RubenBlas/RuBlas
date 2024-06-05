"""

   Oriol Barba Vázquez
   03/10/2022
   ASIXc M03 UF1 A3

    Descripció: Introdueix el número de persones i el número de galetes.

    Introdueix el número de persones i el número de galetes.

Si a tothom li toquen el mateix número de galetes imprimeix "Let's Eat!", sinó imprimeix "Let's Fight"

Input

10 20

Output

Let's Eat!

"""

numeroPersona = int(input("Introdueix el numero de persones: "))
numeroGaletes = int(input("Introduiex el numero de galetes: "))

if numeroGaletes%numeroPersona == 0:
    print("Let's Eat!")
else:
    print("No tenen el mateix numero de galetes")
