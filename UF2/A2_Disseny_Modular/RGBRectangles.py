""" Volem fer un programa que dibuixi rectangles de colors a la consola.

Per exemple, si volem que dibuixi els següents 3 rectangles.

color: RED, llargada: 4, amplada: 5
color: YELLOW, llargada: 2, amplada: 2
color: GREEN, llargada: 3, amplada: 5
"""
file = open("colors.txt","rt")
print(file.read())
def ArxiuColors():
    for linea in file:
        print(linea)
ArxiuColors()
contador = 0
def demanar_rectangle():
    prompt = input("")
    return prompt

prompt = demanar_rectangle()

def separar_dades(prompt):
    llista_dades = prompt.split(" ")
    return llista_dades

llista_dades = separar_dades(prompt)
color = llista_dades[0]
filas = llista_dades[1]
columnas = llista_dades[2]
while prompt != ";Q":
    
    prompt = input()