"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e2. Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5

Reconocimiento:  Altura del triangulo > secuencia de texto > separacion entre bordes > base del triangulo

Utilidad: INPUT(Alçada del triangle) > OUTPUT(un conjunt de strings que formen un triangle amb nombres desde el 1 fins la alçada a les cantonades)
"""
"""
"""
try:
    #INPUT(Altura del triangulo)
    Altura = int(input())

    #Secuencia de texto
    if 1 < Altura < 10:
        print("1")
        if 2 < Altura < 10:
            for i in range(Altura-2):
                #Separacion entre bordes
                print(str(i+2)+" "*i+str(i+2))
            #Base del triangulo
            print(str(Altura)*(Altura))
        #Caso excepcional a la funcion anterior
        else:
            print("22")
    else:
        print("Has leido el enunciado? Altura entre 2 i 9.")
except:
    print("Has leido el enunciado? La alzada es un numero")