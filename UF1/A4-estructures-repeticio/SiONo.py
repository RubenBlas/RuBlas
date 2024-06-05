

RespostaUsuari = input("Vols Continuar? s/n ")

if RespostaUsuari.upper() == "N" or RespostaUsuari.upper() == "S":

    while RespostaUsuari.upper() == "N":
        RespostaUsuari = input("Vols Continuar? s/n ")

else:
    print("Les respostes han de ser s o n")

print("Programa Acabat")