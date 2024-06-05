"""
   Oriol Barba Vázquez
   07/12/2022
   ASIXc M03 UF1 A4
   Descripció: Estructures de Repetició

Demana un enter a l'usuari, per saber quantes línies
Demana un enter a l'usuari, per saber quants punts
Imprimeix per pantalla tantes línies amb tants punts com l'usuari hagi indicat
"""
liniesUsuari = int(input("Quantes linies vols? "))
puntsUsuari = int(input("Quants punts vols? "))

for i in range(liniesUsuari):
    for t in range(puntsUsuari):
        t = "."
        print(t,end="")
    print("")

