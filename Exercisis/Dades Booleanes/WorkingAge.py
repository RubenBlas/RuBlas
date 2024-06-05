"""

   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -WorkingAge

    Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per
    treballar legalment és 16 i suposarem l'edat màxima als 65.

"""
# Creem una variable per guardar la edat de l'Usuari
edatUsuari = int(input("Introdueix la teva edat: "))

# Introduim una condició if/else que indica que la edat del usuari ha d'estar entre els 16 i els 65 per poder treballar.
if  16 <= edatUsuari <= 65:
    print("Tens edat per treballar")
else:
    print("No tens edat per treballar")


