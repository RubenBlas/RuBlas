"""
Oriol Barba Vázquez
24/01/2023
ASIXc M03 UF1 A5
"""
# Declaració de Variables
llista_paraules = []
llista_copiada = []
print(llista_paraules)
llargada_mitjana = 0
for i in range(13):
    paraula = input()
    llista_paraules.append(paraula)
    llargada_mitjana += len(llista_paraules[i])
llargada_mitjana = llargada_mitjana//13
print(llista_paraules)
print("LLargada Mitjana:", llargada_mitjana)
# Si la longitud d'una paraula es equivalent a la llargada mitjana --> Append
for i in llista_paraules:
    if len(i) == llargada_mitjana:
        llista_copiada.append(i)
print(llista_copiada)
