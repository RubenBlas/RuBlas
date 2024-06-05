"""

   Oriol Barba Vázquez/Ruben Blas Lario
   05/10/2022
   ASIXc M03 UF1 A2
   Descripció: A2-Manipulació-de-Dades
   -EOP 3

   EOP 3
Usant un editor de textos, genereu una funció que calculi el pas de graus Celsius a Fahrenheit amb la fórmula: F = (9 / 5) * C + 32

"""

resposta = str(input("Quina mesura vols obtenir? c/f "))

if resposta == "c":
    print("Vols passar el valor de Fahrenheit a Celsius.")
    valorFahrenheit = float(input("Introdueix el Valor: "))

    respostaCelsius = round(((valorFahrenheit - 32)/(9/5)), 1)
    print(str(respostaCelsius)+" Cº")

elif resposta == "f":
    print("Vols passar el valor de Celsius a Fahrenheit.")
    valorCelsius = float(input("Introdueix el Valor: "))

    respostaFahrenheit = round(((9 / 5) * (valorCelsius + 32)), 1)
    print(str(respostaFahrenheit)+"F º")
else:
    print("La resposta ha de ser o 'c' o 'f' ")
