with open("Dragon.in", "r", encoding="UTF-8") as f:
    dragon = f.read()
f.close()
with open("Dragon.out", "w", encoding="UTF-8") as f:
    f.write(dragon.replace("0", "👁"))
f.close()