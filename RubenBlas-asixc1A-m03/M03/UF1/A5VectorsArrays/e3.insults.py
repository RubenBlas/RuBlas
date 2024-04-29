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


insult = (input())
insult = insult.upper
traducciones = {
    "ARALLOT": ("AGALLADO", "SCOUNDREL", "HOREY'SO"),
    "MALPARIT": ("MALPARIDO", "WRETCHED", "PU'HICH"),
    "TROS DE QUÒNIAM": ("TROZO DE COJÓN", "PIECE OF TESTICLE", "QI'TU'"),
    "FLASCA": ("BOTELLA", "BOTTLE", "JE'"),
    "TARAL·LIROT": ("TRIPATRAZADO", "DIMWIT", "· NGIQ"),
    "LLONDRO": ("TONTOLABA", "FOOL", "RON"),
    "ABRAÇAFANALS": ("ABRAZAFANOS", "HUGGERMUGGER", "TAP"),
    "AFAITAPAGESOS": ("AFILAHOCICOS", "LANDLUBBER", "SIQWI'"),
    "BORDEGÀS": ("BORRACHÍN", "DRUNKARD", "BORDEGÀS"),
    "BOTIFLER": ("TRAIDOR", "TRAITOR", "CHE'WI'"),
    "ESTAQUIROT": ("CAGATIÓ", "SHITHEAD", "ROSEN"),
    "BALIGA-BALAGA": ("BOLSAPERA", "BAGPUSHER", "BIQ"),
    "BAGASSA": ("PUTA", "WHORE", "NGOJ"),
    "BRÈTOL": ("ZOQUETE", "DIMWIT", "LIW"),
    "GALIFARDEU": ("GALLINACEO", "CHICKEN", "CHE'RON"),
    "LLEPACULS": ("LAMECULOS", "ASS-KISSER", "NUTLH"),
    "BENEIT": ("BENDITO", "BLESSED", "QIp"),
    "PIXAPINS": ("MEONCILLO", "PISSTAKER", "JUS"),
    "BLEDA ASSOLELLADA": ("COL LECHUGA", "LETTUCE HEAD", "CHOQAD"),
    "SÒMINES": ("CERDITO", "PIGGY", "VAY'"),
    "ENZE": ("IDO", "GONE", "TAH"),
    "CAMACURT": ("COJO", "LAME", "MUV"),
    "CAPSIGRANY": ("CABECITA DE GAMBA", "SHRIMP HEAD", "DEGHWI'"),
    "CURT DE GAMBALS": ("CHOCHOFLOR", "PUSSYFLOWER", "QORDU'"),
    "FIGAFLOR": ("ZANAHORIA", "CARROT", "SEQ"),
    "PASTANAGA": ("TETA", "TIT", "qe'rot 'oQqar"),
    "TANOCA": ("DOLT", "TINY PLANET", "SUVLAHBE'"),
    "TÒTIL": ("TONTORRÓN", "HOOLIGAN", "PUCH"),
    "LLANUT": ("PLANETILLA", "BOOR", "QIM"),
    "GAMARÚS": ("GAMBERRO", "PALURDO", "GAMARÚS"),
    "PALLÚS": ("PALLURDO", "VAGO", "QAD"),
    "DROPO": ("VAGO", "LAZYBONES", "'orwI'"),
    "PÒTOL": ("CABEZA DE SUCRO", "CORK HEAD", "TALÓS"),
    "TALÓS": ("POLLITO", "CHICKEN", "BAQ"),
    "TRINXERAIRE": ("ABUSADOR", "ABUSER", "Dogh"),
    "CAP DE SURO": ("BARBAMEC", "BARBAMEC", "CHUS"),
    "POLLÓS": ("POLLITO", "CHICKEN", "LODNAL"),
    "ABUSANANOS": ("ABUSADOR", "ABUSER", "ROL"),
    "BARBAMEC": ("BARBAMEC", "BARBAMEC", "TOR"),
    "PINXO": ("STICK", "POT ASS", "qa'rI'"),
    "CUL D'OLLA": ("CULO DE OLLA", "SHIT BANDIT", "'URSANAB"),
    "CAGABANDÚRRIES": ("CAGADOR DE MIERDA", "SHITTER", "CHELWI'"),
    "CAGANER": ("CAGÓN", "HALF-SHIT", "BOQ"),
    "MITJA MERDA": ("MEDIA MIERDA", "NAP-BUF", "QIH"),
    "NAP-BUF": ("NAP-BUF", "NAP-BUF", "BIQ"),
    "BORINOT": ("BORINOT", "BORINOT", "tlhagh"),
    "TITELLA": ("MARIONETA", "PUPPET", "GHAYTI'"),
    "CAGADUBTES": ("DUDADOR DE MIERDA", "SHIT DOUBTER", "'EJ RATLHQU'"),
    "POCA-TRAÇA": ("POCA TRAZA", "LITTLE TRACE", "QI'TU'"),
    "SAPASTRE": ("SASTRE", "TAILOR", "roS"),
    "LLEPAFILS": ("LAMEHILOS", "LICKTHREADS", "QEYHA'"),
    "POCA-SOLTA": ("POCA SUELTA", "LOOSE THREAD", "NYÈBIT"),
    "NYÈBIT": ("ÑEBE", "NUISANCE", "NYÈBIT"),
    "CAP DE TRONS": ("CABEZA DE TRUENO", "THUNDER HEAD", "NADEV NGOD"),
    "BANYUT": ("BAÑADO", "BATHED", "GHEB"),
    "CALÇASSES": ("CALZONAZOS", "PANTYWAIST", "CALÇASSES")
}

if insult in traducciones:
    print(f"En català: " + insult)
    print(f"En castellà: {traducciones[insult][0]}")
    print(f"En anglès: {traducciones[insult][1]}")
    print(f"En klingon: {traducciones[insult][2]}")
else:
    print(f"Insult '{insult}' no trobat.")