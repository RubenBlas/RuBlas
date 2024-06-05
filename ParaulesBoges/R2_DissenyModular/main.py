"""
Gerard Cano Maneja Oriol Barba Ruben Blas
15/2/2023
ASIXc M03 UF2
Descripció: R1:Disseny descendent i dividir en funcions
"""
from dataSource import *
from crazyWords import getCrazy

print('Elige una opcion:')
print('Teclado: 1, Server: 2, ChatGPT: 3')
opcion = int(input())

if opcion == 1:
    fraseTeclado = getDataFromKeyboard()
    getCrazy(fraseTeclado)
elif opcion == 2:
    fraseServer = getDataFromServer(input("Introduce una URL: "))
    getCrazy(fraseServer)
elif opcion == 3:
    fraseCHATGPT = getDataFromChatGPT(input("Introduce una pregunta: "))
    getCrazy(str(fraseCHATGPT))
else:
    print("OPCION FUERA DEL RANGO")
