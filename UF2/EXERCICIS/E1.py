"""
Asixc1A
Calcular quants signes de puntuació té una cadena de text qualsevol (és a dir no necessàriament una paraula)
Exemple:
Què, qui ? com? No ho sé!.
5 signes de puntuació
(Hem d'utilitzar el Codi ASCII)
"""
string_usuari = input()
def contar_signes():
    cont = 0
    for i in string_usuari:
        if 33 <= ord(i) <= 47 or 58 <= ord(i) <= 63:
            cont += 1
    print(cont)
contar_signes()


