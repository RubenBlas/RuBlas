import os
import stat
import datetime

def verificar_existencia_ruta(ruta):
    if os.path.exists(ruta):
        if os.path.isfile(ruta):
            print(f"La ruta {ruta} existe y es un archivo.")
        elif os.path.isdir(ruta):
            print(f"La ruta {ruta} existe y es un directorio.")
    else:
        print(f"La ruta {ruta} no existe.")

def listar_contenido_directorio(directorio):
    if os.path.exists(directorio) and os.path.isdir(directorio):
        print(f"Contenido de {directorio}:")
        for item in os.listdir(directorio):
            print(item)
    else:
        print(f"El directorio {directorio} no existe o no es válido.")

def gestionar_directorio_archivo(ruta):
    # Aquí implementar las funciones de gestión de directorios y archivos
    pass

def mostrar_directorios_padre(ruta):
    while True:
        ruta_padre = os.path.dirname(ruta)
        if ruta_padre == ruta:
            break
        print(f"Directorio padre: {ruta_padre}")
        ruta = ruta_padre

def mostrar_contenido_directorio(ruta):
    # Aquí implementar la función para mostrar información detallada de archivos y directorios
    pass
