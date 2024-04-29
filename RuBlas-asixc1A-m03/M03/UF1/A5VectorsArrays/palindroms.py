"""
Ruben Blas Lario
29/01/2024 - M03 UF1 Pr5

Indica si una paraula és palíndrom.


Exemples de palíndroms: cec, cuc, gag, mínim, nan, nen, pipiripip…

juntar las palabras

"""
palindrom = str(input())
palindromSplit = palindrom.split(" ")
palindrom = ""
for i in palindromSplit:palindrom += i
if palindrom == palindrom[::-1]: print("es")
else: print("no es")

#Solo esta hecho para quitar espacios