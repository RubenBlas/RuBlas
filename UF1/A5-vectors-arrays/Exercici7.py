"""
Escriu un programa que declari tres llistes “llista1”, “llista2” i “llista3”,
amb cinc sencers cadascuna, i que demani valors per a “llista1” i “llista2”.
El programa ha d'emplenar llavors llista3 de manera que contingui la suma dels elements de ‘llista1’ i ‘llista2’.
Per exemple, donades aquestes llistes:
llista1 = [23,54,-12,0,70]
llista2 = [543,-234,5,11,20]
‘llista3’ ha de tenir aquests elements:
llista3 = [566,-180,-7,11,90]

"""
import random
RANGO_LISTA = 5
llista_1 = [random.randint(1,1000) for i in range(RANGO_LISTA)]
llista_2 = [random.randint(1,1000) for i in range(RANGO_LISTA)]
llista_3 = []
for i in range(len(llista_2)):
    llista_3.append(llista_1[i] + llista_2[i])
print("Primera llista:",llista_1)
print("segonda llista:",llista_2)
print("Resultat:",llista_3)