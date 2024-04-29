"""
# Crear una tabla bidimensional usando listas anidadas
tabla = []

filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

# Llenar la tabla con datos
for y in range(filas):
    # Crear una nueva fila (una lista vacía) en cada iteración
    fila = []
    
    for x in range(columnas):
        # Agregar elementos a la fila usando append()
        fila.append(x)
    
    # Agregar la fila completa a la tabla usando append()
    tabla.append(fila)

# Mostrar la tabla
for fila in tabla:
    print(fila)
"""
# Crear una tabla bidimensional usando listas anidadas con tuplas vacías
tabla = []

filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

# Llenar la tabla con tuplas vacías
for y in range(filas):
    # Crear una nueva fila (una lista vacía de tuplas) en cada iteración
    fila = [() for _ in range(columnas)]
    
    # Agregar la fila completa a la tabla usando append()
    tabla.append(fila)

# Mostrar la tabla
for fila in tabla:
    print(fila)
