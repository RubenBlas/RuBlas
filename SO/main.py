import file_manager
import search

def main():
    print("Bienvenido al gestor de archivos.")

    while True:
        print("\nMenú:")
        print("1. Verificar existencia de ruta")
        print("2. Listar contenido de directorio")
        print("3. Gestionar directorio/archivo")
        print("4. Mostrar directorios padres")
        print("5. Mostrar contenido detallado de directorio")
        print("6. Buscar archivos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            verificar_ruta()
        elif opcion == "2":
            listar_contenido_directorio()
        elif opcion == "3":
            gestionar_directorio_archivo()
        elif opcion == "4":
            mostrar_directorios_padre()
        elif opcion == "5":
            mostrar_contenido_detallado_directorio()
        elif opcion == "6":
            buscar_archivos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def verificar_ruta():
    ruta = input("Introduce el nombre de un archivo o directorio: ")
    file_manager.verificar_existencia_ruta(ruta)

def listar_contenido_directorio():
    directorio = input("Introduce el nombre de un directorio: ")
    file_manager.listar_contenido_directorio(directorio)

def gestionar_directorio_archivo():
    ruta = input("Introduce la ruta de un directorio o archivo: ")
    file_manager.gestionar_directorio_archivo(ruta)

def mostrar_directorios_padre():
    ruta = input("Introduce una ruta de directorio: ")
    file_manager.mostrar_directorios_padre(ruta)

def mostrar_contenido_detallado_directorio():
    ruta = input("Introduce la ruta de un directorio: ")
    file_manager.mostrar_contenido_directorio(ruta)

def buscar_archivos():
    directorio_origen = input("Introduce el directorio de origen: ")
    extension = input("Introduce la extensión del archivo (si no deseas filtrar por extensión, déjalo en blanco): ")
    nombre = input("Introduce el nombre del archivo (si no deseas filtrar por nombre, déjalo en blanco): ")
    oculto = input("¿Deseas buscar archivos ocultos? (si / no): ").lower()
    if oculto == "si":
        oculto = True
    else:
        oculto = False
    search.buscar_archivos(directorio_origen, extension, nombre, oculto)

if __name__ == "__main__":
    main()
