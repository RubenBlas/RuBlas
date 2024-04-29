try:    
    abrir = int(input())
    cajas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while abrir != -1:
            if 0 <= abrir < 10:  
                cajas[abrir] += 1
            abrir = int(input())
    print(cajas)
except ValueError:
    print("Esa caja no forma parte del banco")

#falla por no hacerlo en columnas