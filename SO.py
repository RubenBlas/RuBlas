import os
import stat
import time
import shutil


def comprovar_existencia(nom):
    """Comprova si un fitxer o directori existeix i mostra la seva informació."""
    if os.path.exists(nom):
        if os.path.isfile(nom):
            print(f"'{nom}' és un fitxer.")
        elif os.path.isdir(nom):
            print(f"'{nom}' és un directori.")

        ruta_absoluta = os.path.abspath(nom)
        ruta_relativa = os.path.relpath(nom)
        print(f"Ruta absoluta: {ruta_absoluta}")
        print(f"Ruta relativa: {ruta_relativa}")
    else:
        print(f"'{nom}' no existeix.")


def llistar_contingut_directori(directori):
    """Llista les carpetes i fitxers d'un directori donat."""
    if os.path.exists(directori) and os.path.isdir(directori):
        contingut = os.listdir(directori)
        print(f"Contingut de '{directori}':")
        for element in contingut:
            ruta_completa = os.path.join(directori, element)
            if os.path.isfile(ruta_completa):
                print(f"  [Fitxer] {element}")
            elif os.path.isdir(ruta_completa):
                print(f"  [Directori] {element}")
    else:
        print(f"'{directori}' no existeix o no és un directori.")


def crear_element():
    """Crea un fitxer o directori nou."""
    tipus = input("Vols crear un fitxer o un directori? (f/d): ")
    nom = input("Introdueix el nom del fitxer o directori a crear: ")
    if tipus == 'f':
        with open(nom, 'w') as fitxer:
            fitxer.write("")  # Crear un fitxer buit
        print(f"Fitxer '{nom}' creat.")
    elif tipus == 'd':
        os.mkdir(nom)
        print(f"Directori '{nom}' creat.")
    else:
        print("Opció no vàlida.")


def esborrar_element():
    """Esborra un fitxer o directori."""
    nom = input("Introdueix el nom del fitxer o directori a esborrar: ")
    if os.path.exists(nom):
        if os.path.isfile(nom):
            os.remove(nom)
            print(f"Fitxer '{nom}' esborrat.")
        elif os.path.isdir(nom):
            os.rmdir(nom)
            print(f"Directori '{nom}' esborrat.")
    else:
        print(f"'{nom}' no existeix.")


def canviar_nom_element():
    """Canvia el nom d'un fitxer o directori."""
    nom_actual = input("Introdueix el nom actual del fitxer o directori: ")
    nom_nou = input("Introdueix el nou nom del fitxer o directori: ")
    if os.path.exists(nom_actual):
        os.rename(nom_actual, nom_nou)
        print(f"'{nom_actual}' s'ha renombrat a '{nom_nou}'.")
    else:
        print(f"'{nom_actual}' no existeix.")


def canviar_permisos_element():
    """Canvia els permisos d'un fitxer o directori."""
    nom = input("Introdueix el nom del fitxer o directori: ")
    if os.path.exists(nom):
        permisos = int(input("Introdueix els nous permisos (en octal, p. ex. 755): "), 8)
        os.chmod(nom, permisos)
        print(f"Permisos de '{nom}' canviats a {oct(permisos)}.")
    else:
        print(f"'{nom}' no existeix.")


def mostrar_directoris_pares():
    """Mostra els directors pares fins a arribar a l'arrel."""
    directori = input("Introdueix el nom del directori: ")
    if os.path.exists(directori) and os.path.isdir(directori):
        print("Directoris pares:")
        while True:
            directori_pare = os.path.dirname(directori)
            if directori == directori_pare:
                break
            print(directori)
            directori = directori_pare
        print(directori)  # Finalment, mostra l'arrel
    else:
        print(f"'{directori}' no existeix o no és un directori.")


def llistar_detalls_directori(directori):
    """Llista les carpetes i fitxers d'un directori donat amb detalls."""
    if os.path.exists(directori) and os.path.isdir(directori):
        print(f"Contingut detallat de '{directori}':")
        for root, dirs, files in os.walk(directori):
            for nom in dirs:
                ruta_completa = os.path.join(root, nom)
                estat = os.stat(ruta_completa)
                data_modificacio = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(estat.st_mtime))
                espai_lliure = shutil.disk_usage(ruta_completa).free
                permisos = oct(estat.st_mode)[-3:]
                print(f"[Directori] {ruta_completa}")
                print(f"  Espai lliure: {espai_lliure} bytes")
                print(f"  Data modificació: {data_modificacio}")
                print(f"  Permisos: {permisos}")

            for nom in files:
                ruta_completa = os.path.join(root, nom)
                estat = os.stat(ruta_completa)
                mida = estat.st_size
                data_modificacio = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(estat.st_mtime))
                permisos = oct(estat.st_mode)[-3:]
                print(f"[Fitxer] {ruta_completa}")
                print(f"  Mida: {mida} bytes")
                print(f"  Data modificació: {data_modificacio}")
                print(f"  Permisos: {permisos}")
    else:
        print(f"'{directori}' no existeix o no és un directori.")


def cercador_fitxers(directori, extensio=None, nom=None, ocults=None):
    """Cerca fitxers en un directori basat en criteris de filtre."""
    if os.path.exists(directori) and os.path.isdir(directori):
        print(f"Resultats de la cerca a '{directori}':")
        for root, dirs, files in os.walk(directori):
            for file in files:
                ruta_completa = os.path.join(root, file)
                if extensio and not file.endswith(extensio):
                    continue
                if nom and nom not in file:
                    continue
                if ocults is not None:
                    es_ocult = file.startswith('.')
                    if ocults and not es_ocult:
                        continue
                    if not ocults and es_ocult:
                        continue
                estat = os.stat(ruta_completa)
                mida = estat.st_size
                data_modificacio = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(estat.st_mtime))
                permisos = oct(estat.st_mode)[-3:]
                print(f"[Fitxer] {ruta_completa}")
                print(f"  Mida: {mida} bytes")
                print(f"  Data modificació: {data_modificacio}")
                print(f"  Permisos: {permisos}")
    else:
        print(f"'{directori}' no existeix o no és un directori.")


# Funció principal per interactuar amb l'usuari
def main():
    while True:
        print("\nOpcions:")
        print("1. Comprovar existència d'un fitxer o directori")
        print("2. Llistar contingut d'un directori")
        print("3. Crear un fitxer o directori")
        print("4. Esborrar un fitxer o directori")
        print("5. Canviar el nom d'un fitxer o directori")
        print("6. Canviar els permisos d'un fitxer o directori")
        print("7. Mostrar directors pares")
        print("8. Llistar contingut detallat d'un directori")
        print("9. Cercador de fitxers")
        print("10. Sortir")

        opcio = input("Selecciona una opció (1-10): ")

        if opcio == '1':
            nom = input("Introdueix el nom del fitxer o directori: ")
            comprovar_existencia(nom)
        elif opcio == '2':
            directori = input("Introdueix el nom del directori per llistar el seu contingut: ")
            llistar_contingut_directori(directori)
        elif opcio == '3':
            crear_element()
        elif opcio == '4':
            esborrar_element()
        elif opcio == '5':
            canviar_nom_element()
        elif opcio == '6':
            canviar_permisos_element()
        elif opcio == '7':
            mostrar_directoris_pares()
        elif opcio == '8':
            directori = input("Introdueix el nom del directori per llistar el seu contingut detallat: ")
            llistar_detalls_directori(directori)
        elif opcio == '9':
            directori = input("Introdueix el directori d'origen per a la cerca: ")
            extensio = input("Introdueix l'extensió del fitxer a cercar (deixa en blanc si no vols filtrar per extensió): ")
            nom_fitxer = input("Introdueix el nom del fitxer a cercar (deixa en blanc si no vols filtrar per nom): ")
            ocults = input("Vols incloure fitxers ocults? (s/n): ")
            ocults = True if ocults.lower() == 's' else False
            cercador_fitxers(directori, extensio, nom_fitxer, ocults)
        elif opcio == '10':
            break
        else:
            print("Opció no vàlida.")
main()