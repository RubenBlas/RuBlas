"""
Ruben Blas Lario
12/01/2024
ASIXc M03
Descripio: dayOfWeek
Donat un enter, mostrar el dia de la setmana amb text (dilluns, dimarts, dimecres…), tenint en compte que dilluns és el 1. Els dies de la setmana es guarden en una llista.

Fer el control d'errors

Input

7 


Output

diumenge



Execució en "mode usuari". És a dir, del 1 al 7
"""
try:
    DiaNum = int(input())
    Idioma = int(input("Escoge entre: 1. Catalan 2. Ingles 3. Español"))
    DiaStrCat = ["", "Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Disapta", "Diumenge"]
    DayStrNet = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    DiaStrEs = ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Disapta", "Domingo"]
    if 1 == Idioma:
        if 1 <= DiaNum <= 7:
            print(DiaStrCat[DiaNum])
    if 2 == Idioma:
        if 1 <= DiaNum <= 7:
            print(DayStrNet[DiaNum])
    if 3 == Idioma:
        if 1 <= DiaNum <= 7:
            print(DiaStrEs[DiaNum])
except ValueError:
    print("Dades no válides")


