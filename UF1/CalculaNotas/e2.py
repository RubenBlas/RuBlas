"""
Exercici 2
Crear un programa que sigui capaç de calcular la nota final de la UF2 del mòdul 03
del Cicle de Grau Superior d'Administració de Sistemes Informàtics en Xarxa (CFGS ASIX).
 El programa només haurà de fer el càlcul per a 1 estudiant, i mostra'ls per pantalla.
  Les notes de cadascun dels estudiants s'haurà de demanar per pantalla. La fórmula de
   la UF2 és: QUF2 =1*RA1 a on  RA1= 0,15*Pt1.1 + 0,15*Pr1.2+0,70*Pp1.  El pes de cada
    IA està fitxat a l'inici de curs per a no ser modificat. La nota final de les UF's
    es calcula amb 2 decimals.
"""

# Introduim les variables que posarà l'usuari
practicaT1 = float(input("Introdueix la nota de la activitat de projecte: "))
practicaP1 = float(input("Introdueix la nota de la prova practica: "))
practicaR1 = float(input("Introdueix la nota de la practica: "))

# Calculem el resultat de la RA1 i el de QUF2
resultatAprenentatge1 = (0.15 * practicaT1) + (0.15 * practicaR1) + (0.70 * practicaP1)
qualificacioUF2 = round((1 * resultatAprenentatge1), 2)

# Imprimim per pantalla el valor de la QUF2
print("La teva nota de la UF2 es: " + str(qualificacioUF2))
