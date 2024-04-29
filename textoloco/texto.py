def in_texto():
    with open("texto.in", "r") as f:
        texto = f.read()
        f.close("texto.in")
    return texto

def out_texto(texto):
    with open("texto.out", "w") as f:
        f.write(texto)
        f.close("texto.out")
