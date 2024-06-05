"""
   Oriol Barba Vázquez
   13/12/2022
   ASIXc M03 UF1 PP2
   Descripció: Estructures de Repeticio
   Programa que demana a l'usuari les notes (sense decismals) d'11 alumnes.
   El programa ens dirà quantes notes són suspesos i quantes aprovades, mostrant el seu conjunt de notes.
   Cal fer el control de errors.
"""
# Declaramos las variables corresponientes y los contadores
notesAlumnes = input()
notesIndividuals = notesAlumnes.split(" ")
contadorSuspesos = 0
contadorAprovats = 0
# Comprovamos cada nota si es mayor o menor que 5
for i in notesIndividuals:
    if "5" > i > "0":
        contadorSuspesos += 1
    else:
        contadorAprovats += 1
print(":( Suspesos:",contadorSuspesos)
print(":) Aprovats:",contadorAprovats)