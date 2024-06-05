"""
Oriol Barba Vázquez
24/01/2023
ASIXc M03 UF1 A5
"""
# Declaració de Variables
SECRET = "/exit"
frase_usuari = input()
LLISTA_VOCALS = ("a", "e", "i", "o", "u")
LLISTA_NUMEROS = ("1", "2", "3", "4", "5")
cont = 0
# Bucle 'infinit' fins que fem la comanda /exit
while frase_usuari != "/exit":
    nova_frase = ""
    frase_usuari = frase_usuari.lower()
    frase_cript = list(frase_usuari)
    for i in frase_cript:
        for t in range(len(LLISTA_VOCALS)):
            if i == LLISTA_VOCALS[t]:
                frase_cript[frase_cript.index(i)] = LLISTA_NUMEROS[t]
        nova_frase += frase_cript[cont]
        cont += 1
    cont = 0
    print(nova_frase)
    frase_usuari = input()
