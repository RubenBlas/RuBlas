"""
Ruben Blas Lario
02/02/2024 - M03 UF1 PP3 - E3 Mida de les PARAULES- mitjana

Objetivo:
INPUT
-
OUTPUT
-

Proceso:
-
-
-
-

"""
Paraules = 333
emmagatzem = [""]*Paraules
contadorParaules = 0
contadorLen = 0
contador = 0
for i in range(len(emmagatzem)):
    paraula = input()
    if paraula != "/q":
        emmagatzem[i] = paraula
        contadorLen += len(paraula)

        if paraula != "":
            contadorParaules += 1
    else:
        i = len(emmagatzem) + 1
        print(emmagatzem)
        print(contadorLen/contadorParaules)
""" EN ESA PARTE CREA LA TUPLA CON LAS PALABRAS PEQUEÑAS
tuplaPetita = [""]*contadorParaules
for i in emmagatzem:
    paraula = i
    if len(paraula) < contadorLen:
        tuplaPetita[contador] = paraula + ":" +str(len(paraula))
    contador =+ 1
print(tuplaPetita)"""