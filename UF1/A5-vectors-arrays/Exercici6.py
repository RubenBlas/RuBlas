"""
Escriu un programa que demani un número a l'usuari un número de mes (per exemple, el 4, és a dir)
El programa ha de validar que el nombre de mes sigui entre 1 i 12, si no és així ha de mostrar un missatge d'error
i preguntar novament fins que l'usuari introdueixi un número de mes vàlid. Un cop obtingueu un nombre de mes
 correcte, el programa mostrarà per pantalla quants dies té el mes (al nostre exemple, 30) i el nom del mes
  (a l'exemple, abril). Has de fer servir llistes. Per simplificar suposarem que el febrer sempre té 28 dies.
"""
try:
    numeroUsuari = int(input())
    while 1 <= numeroUsuari <= 12:
        print("Correcte")
    else:
        print("Numero fora de Rang")

except:
    print("Ha donat ERROR")
