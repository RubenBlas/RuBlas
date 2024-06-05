"""

   Oriol Barba Vázquez
   03/10/2022
   ASIXc M03 UF1 A3

   Descripció: Demana dos enters a l'usuari i imprimeix el valor més gran

   Estructures de Repetició
"""

a = int(input("Escriu el primer numero: "))
b = int(input("Escriu el segon numero: "))

# bAquest condicional IF/ELSE ens dona a entendre que nomes imprimirà el numero més gran
if a > b:
    print(a)
elif a == b:
    print("Els numeros son iguals")
else:
    print(b)