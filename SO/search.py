import os

def buscar_archivos(directorio, extension=None, nombre=None, oculto=None):
    archivos_encontrados = []
    for ruta, carpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(ruta, archivo)
            if extension is not None and not archivo.endswith(extension):
                continue
            if nombre is not None and nombre not in archivo:
                continue
            if oculto is not None and oculto != archivo.startswith('.'):
                continue
            archivos_encontrados.append(ruta_completa)
    print("Archivos encontrados:")
    for archivo in archivos_encontrados:
        print(archivo)
