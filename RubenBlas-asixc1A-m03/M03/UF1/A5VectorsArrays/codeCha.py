palabra = input()
lista = len(palabra)*[""]

for i in range(len(palabra)):
    lista[i] += palabra[i]
print(lista)


palabra = ""

for i in range(len(lista)):
    palabra += (lista[i])
print(palabra)