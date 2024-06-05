"""
Gerard Cano Maneja Oriol Barba Ruben Blas
25/04/2023
ASIXc M03 UF3
Descripció: R3:Disseny per Fitxers
"""
from crazyWords import getCrazy
import time
import os
temps_real = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())

ruta = './'
archiusEntrada = []
archiusSortida = []
frases = []
# Recorremos el directorio con os.walk()
for directorio_actual, subdirectorios, archivos in os.walk(ruta):
    for i in archivos:
        if 'Boges' not in i and 'entrada' in i:
            archiusEntrada.append(str(i))
            archiusEntrada.sort()
print(archiusEntrada)

for t in archiusEntrada:
    with open(t) as f:
        input = f.read()
        frases.append(input)
    print(frases)
    nomArchiu = t.split(".")
    nomArchiu.insert(1,'Bojes.')
    nomArchiu = "".join(nomArchiu)
    archiusSortida.append(nomArchiu)
    archiusSortida.sort()
print(archiusSortida)

time.sleep(1)
print("Crazing Words...")
time.sleep(1)
for num,file in enumerate(archiusSortida):
    with open(file,"w") as f:
        with open("error.log","a") as log:
            try:

                output = f.write(getCrazy(frases[num]))

                log.write(temps_real+' - Frase Crazed correctament' + ' - DEBUG MESSAGE - '+ str(time.time()/(10*pow(10, 9))) + ' s\n')
            except IndexError:
                log.write(temps_real+' - Index de la frase incorrecte' + ' - WARNING MESSAGE - '+ str(time.time()/(10*pow(10, 9))) + ' s\n')
            except OSError:
                log.write(temps_real+' - Error en el sistema' + ' - ERROR MESSAGE - '+ str(time.time()/(10*pow(10, 9))) + ' s\n')
            except SystemExit:
                log.write(temps_real+' - Sortint del sistema' + ' - ERROR MESSAGE - '+ str(time.time()/(10*pow(10, 9))) + ' s\n')

