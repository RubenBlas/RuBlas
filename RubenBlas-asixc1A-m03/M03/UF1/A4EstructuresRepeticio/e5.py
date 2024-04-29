"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e5. Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes

"""
try:
    #Introduccio de numeros
    numeros = input()
    numeros = numeros.split(" ")
    #Variables
    n1 = abs(int(numeros[0]))
    n2 = abs(int(numeros[1]))
    multiplicacio = 0

    #Programa
    for i in range(n2):
        #Multiplicació
        multiplicacio = multiplicacio + n1

    print(multiplicacio)
except ValueError:
    print("Dades no válides")