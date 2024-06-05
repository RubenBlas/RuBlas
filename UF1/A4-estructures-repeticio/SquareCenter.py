"""
 Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
   Descripció: Estructures de Repetició

Fes una funció que dibuixi dos quadrats concèntrics. l'usuari introdueix dos valors, el primer defineixen el
 costat del quadrat extern que pintarem amb o, el segon defineix el costat del segon quadrat. Aquest segon quadrat
  el pintarem amb *.
"""
primerQuadrat = int(input())
segonQuadrat = int(input())
CENTRE = "🔥"
ARBRE = "🌳"
separacio = (primerQuadrat - segonQuadrat)//2

for i in range(primerQuadrat):
    for j in range(primerQuadrat):
        if separacio <= i <= separacio + segonQuadrat-1 and separacio <= j <= separacio + segonQuadrat-1:
            print(CENTRE,end="")
        else:
            print(ARBRE,end="")
    print("")


