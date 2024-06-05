from datetime import date
from datetime import datetime
from time import sleep

def obteOpcio():
    print("1. Primera Opcio")
    print("2. Millor Opcio")
    print("3. Tractar Error")
    print("4. Tractament Final")
    return int(input())

def opcioPrimera():
    print("La primera opcio!")
    sleep(1)

def opcioLaMillor():
    print("La millor opcio!")
    sleep(1)

def tractarError():
    hora = datetime.now()
    hora = hora.strftime("%d %m %Y %H:%M:%S")
    print(f"{hora} --> ERROR")

def tractamentFinal():
    print("FINAL")

opcio = obteOpcio()

while opcio != 4:
    if opcio < 1 or opcio > 3:
        print("Numero fora del rang.")
    else:
        if opcio == 1:
            opcioPrimera()
        elif opcio == 2:
            opcioLaMillor()
        elif opcio == 3:
            tractarError()
    opcio = obteOpcio()

tractamentFinal()

