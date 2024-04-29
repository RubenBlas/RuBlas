"""
Ruben Blas Lario
29/01/2024 - M03 UF1 Pr5

Indica si una paraula és palíndrom.


Exemples de palíndroms: cec, cuc, gag, mínim, nan, nen, pipiripip…


"""
palindroms = str(input())
palindrom = palindroms.split(" ")
for i in palindrom:
    if palindrom == palindrom[::-1]: print("es")
    else: print("no es")
