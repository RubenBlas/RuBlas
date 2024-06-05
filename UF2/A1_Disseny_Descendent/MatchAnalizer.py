"""
MatchAnalizer

1. Partit de Basquet ---> 1 punt , 2 punts i 3 punts

Si 1 punt --> Tir lliure
Si 2 punts --> Cistella
Si 3 punts --> Triple

1 Equip -- 2 Equip

Si -1 --> Acaba el partit
"""
marcadorA = []
marcadorB = []


def puntuacions():
    equipLocal = input()
    equipVisitant = input()
    puntuacio = input()

    while puntuacio != "-1":
        contadorA = 0
        contadorB = 0
        marcadorA.append(puntuacio[0])
        marcadorB.append(puntuacio[2])
        if len(marcadorA) == 1 and len(marcadorB) == 1:
            if marcadorA[-1] == "1":
                print("Tir lliure de " + equipLocal)
            elif marcadorA[-1] == "2":
                print("Cistella de " + equipLocal)
            elif marcadorA[-1] == "3":
                print("Triple de " + equipLocal)
            elif marcadorB[-1] == "1":
                print("Tir lliure de " + equipVisitant)
            elif marcadorB[-1] == "2":
                print("Cistella de " + equipVisitant)
            elif marcadorB[-1] == "3":
                print("Triple de " + equipVisitant)
        if (len(marcadorA) >= 2 and len(marcadorB) >= 2):
            puntAanterior = int(marcadorA[-1]) - int(marcadorA[-2])
            puntBanterior = int(marcadorB[-1]) - int(marcadorB[-2])
            if puntAanterior == 1:
                print("Tir lliure de " + equipLocal)
            elif puntAanterior == 2:
                print("Cistella de " + equipLocal)
            elif puntAanterior == 3:
                print("Triple de " + equipLocal)
            elif puntBanterior == 1:
                print("Tir lliure de " + equipVisitant)
            elif puntBanterior == 2:
                print("Cistella de " + equipVisitant)
            elif puntBanterior == 3:
                print("Triple de " + equipVisitant)
        puntuacio = input()

# Introduim el nom dels equips
puntuacions()