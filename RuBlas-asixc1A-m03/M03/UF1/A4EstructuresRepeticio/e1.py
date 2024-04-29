"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

Programa que demana a l'usuari la introducció de 10 nombres sencers (que també podrien
ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla, quants són positius,
quants negatius i quants zero.

Reconocimiento: Introduccion de numeros > Cuantos son positivos > Cuantos son negativos > Cuantos son cero

Utilidad: INPUT(Introduccion de numeros) > OUTPUT(Cantidad de positivos, negativos y ceros)
"""




#Contadores p=positivo, n=negativo, z=0
p=0
n=0
z=0

for i in range(10):
    try:
        # Introduccion de numeros
        numero = int(input(""))
        # Cuantos son positivos
        if numero > 0:
            p = p + 1
        # Cuantos son cero
        elif numero == 0:
            z = z + 1
        # Cuantos son negativos
        else:
            n = n + 1
        print("Hay ", p, "numeros positivos,", n, "numeros negativos y", z, "zeros")

    except ValueError:
            print("Datos no validos")




