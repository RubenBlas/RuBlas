"""

   Oriol Barba Vázquez
   15/11/2022
   ASIXc M03 UF1 A4

   Descripció:

   Estructures de Repetició

"""

SECRET = "javiusuari"
contrasenyaUsuari = input("Introdueix la contrasenya: " )

intents = 1
MAX_INTENTS = 5

while intents < MAX_INTENTS and contrasenyaUsuari != SECRET:

    contrasenyaUsuari = input("Introdueix la contrasenya: ")
    intents += 1

if contrasenyaUsuari == SECRET:
    print("Contrasenya Correcta")
else:
    print("Numero de intents superat")

print("Programa Finalitzat")
