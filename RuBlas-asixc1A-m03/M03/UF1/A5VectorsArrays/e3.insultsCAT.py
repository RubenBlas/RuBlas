"""
Ruben Blas Lario, Iker Blazquez Valverde
22/01/2024 - M03 UF1 Pr5

e3. Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà, anglès i klingon.

Exemple
…
print(insults[CAT]) #['Mocos', 'Capsigrany']
print(insults[CAT][0]) #Mocós
print(insults[CAT][1]) #Capsigrany
print(insults[ESP]) #['Mocoso', 'Cabezón']
print(insults[ENG]) #['Brat', 'Stubborn']
print(insults[KLI]) #['Brat', 'Stubborn']
…

Reconocimiento: Numero Aleatorio de 1 a 50 > Crear Lista de 100 > Pares y Impares > Mediana

Utilidad: INPUT(Introduccion de numeros) > OUTPUT(Cantidad de positivos, negativos y ceros)
"""


CAT = 0
ESP = 1
ENG = 2
KLI = 3

insults = [
    ["ARALLOT", "MALPARIT", "TROS DE QUÒNIAM", "FLASCA", "TARAL·LIROT", "LLONDRO", "ABRAÇAFANALS", "AFAITAPAGESOS",
     "BORDEGÀS", "BOTIFLER", "ESTAQUIROT", "BALIGA-BALAGA", "BAGASSA", "BRÈTOL", "GALIFARDEU", "LLEPACULS", "BENEIT",
     "PIXAPINS", "BLEDA ASSOLELLADA", "SÒMINES", "ENZE", "CAMACURT", "CAPSIGRANY", "CURT DE GAMBALS", "FIGAFLOR",
     "PASTANAGA", "TANOCA", "TÒTIL", "LLANUT", "GAMARÚS", "PALLÚS", "DROPO", "PÒTOL", "TALÓS", "TRINXERAIRE",
     "CAP DE SURO", "POLLÓS", "ABUSANANOS", "BARBAMEC", "PINXO", "CUL D’OLLA", "CAGABANDÚRRIES", "CAGANER",
     "MITJA MERDA", "NAP-BUF", "BORINOT", "TITELLA", "CAGADUBTES", "POCA-TRAÇA", "SAPASTRE", "LLEPAFILS", "POCA-SOLTA",
     "NYÈBIT", "CAP DE TRONS", "BANYUT", "CALÇASSES"],
    ["AGALLADO", "MALPARIDO", "TROZO DE COJÓN", "BOTELLA", "TRIPATRAZADO", "TONTOLABA", "ABRAZAFANOS",
     "AFILAHOCICOS", "BORRACHÍN", "TRAIDOR", "CAGATIÓ", "BOLSAPERA", "PUTA", "ZOQUETE", "GALLINACEO",
     "LAMECULOS", "BENDITO", "MEONCILLO", "COL LECHUGA", "CERDITO", "IDO", "COJO", "CABECITA DE GAMBA",
     "CHOCHOFLOR", "ZANAHORIA", "TETA", "DOLT", "TONTORRÓN", "PLANETILLA", "GAMBERRO", "PALLURDO", "VAGO",
     "CABEZA DE SUCRO", "POLLITO", "ABUSADOR", "BARBAMEC", "POLLITO", "ABUSADOR", "BARBAMEC", "STICK",
     "CULO DE OLLA", "CAGADOR DE MIERDA", "CAGÓN", "MEDIA MIERDA", "NAP-BUF", "BORINOT", "MARIONETA",
     "DUDADOR DE MIERDA", "POCA TRAZA", "SASTRE", "LAMEHILOS", "POCA SUELTA", "ÑEBE", "CABEZA DE TRUENO",
     "BAÑADO", "CALZONAZOS"],
    ["SCOUNDREL", "WRETCHED", "PIECE OF TESTICLE", "BOTTLE", "DIMWIT", "FOOL", "HUGGERMUGGER", "LANDLUBBER",
     "DRUNKARD", "TRAITOR", "SHITHEAD", "BAGPUSHER", "WHORE", "DIMWIT", "CHICKEN", "ASS-KISSER", "BLESSED",
     "PISSTAKER", "LETTUCE HEAD", "PIGGY", "GONE", "LAME", "SHRIMP HEAD", "PUSSYFLOWER", "CARROT", "TIT",
     "TINY PLANET", "HOOLIGAN", "BOOR", "PALURDO", "VAGO", "LAZYBONES", "CORK HEAD", "CHICKEN", "ABUSER",
     "BARBAMEC", "CHICKEN", "ABUSER", "BARBAMEC", "POT ASS", "SHIT BANDIT", "SHITTER", "HALF-SHIT", "NAP-BUF",
     "NAP-BUF", "BORINOT", "PUPPET", "SHIT DOUBTER", "LITTLE TRACE", "TAILOR", "LICKTHREADS", "LOOSE THREAD",
     "NUISANCE", "THUNDER HEAD", "BATHED", "PANTYWAIST"],
    ["HOREY'SO", "'urwI'", "QI'TU'", "JE'", "· NGIQ", "RON", "TAP", "SIQWI'", "BORDEGÀS", "CHE'WI'", "ROSEN",
     "BIQ", "NGOJ", "LIW", "CHE'RON", "NUTLH", "QIp", "JUS", "CHOQAD", "VAY'", "TAH", "MUV", "DEGHWI'", "QORDU'",
     "SEQ", "qe'rot 'oQqar", "SUVLAHBE'", "PUCH", "QIM", "GAMARÚS", "QAD", "'orwI'", "TALÓS", "Dogh", "CHUS",
     "LODNAL", "ROL", "TOR", "qa'rI'", "'URSANAB", "CHELWI'", "BOQ", "QIH", "BIQ", "tlhagh", "GHAYTI'",
     "'EJ RATLHQU'", "QI'TU'", "roS", "QEYHA'", "NYÈBIT", "GHEB", "CALÇASSES"]
]

insulto_usuario = input("Introduce un insulto en catalán: ")

try:
    index_cat = insults[CAT].index(insults)
    print("Traducciones:")
    print("Castellano:", insults[ESP][index_cat])
    print("Inglés:", insults[ENG][index_cat])
    print("Klingon:", insults[KLI][index_cat])
except ValueError:
        print("Insulto no encontrado en la lista.")


