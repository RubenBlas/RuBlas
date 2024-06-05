# exercicis_fitxers.py

def exercici1():
    ruta_fitxer = input("Introdueix la ruta de l'arxiu: ")

    try:
        with open(ruta_fitxer, 'r') as f:
            text = f.read()

        text_modificat = text.swapcase()  # Canvia entre majúscules i minúscules
        with open(ruta_fitxer, 'w') as f:
            f.write(text_modificat)

        print("Contingut de l'arxiu amb majúscules i minúscules intercanviades:")
        print(text_modificat)

    except FileNotFoundError:
        print("Error: No s'ha trobat l'arxiu.")
    except Exception as e:
        print("Error:", e)


def exercici2():
    ruta_fitxer = input("Introdueix la ruta de l'arxiu: ")

    try:
        with open(ruta_fitxer, 'r') as f:
            linies = f.readlines()

        num_linia = 1
        for linia in linies:
            paraules = linia.strip().split()
            num_paraules = len(paraules)
            if linia.strip().lower() != 'fi':
                print(f"La línia {num_linia} té {num_paraules} paraules.")
            num_linia += 1

    except FileNotFoundError:
        print("Error: No s'ha trobat l'arxiu.")
    except Exception as e:
        print("Error:", e)


def exercici3():
    def calcular_histograma(notes):
        histograma = {'Excel·lent': 0, 'Notable': 0, 'Aprovat': 0, 'Suspès': 0}
        for nota in notes:
            if 9 <= nota <= 10:
                histograma['Excel·lent'] += 1
            elif 6.5 <= nota < 9:
                histograma['Notable'] += 1
            elif 5 <= nota < 6.5:
                histograma['Aprovat'] += 1
            elif nota < 5:
                histograma['Suspès'] += 1
        return histograma

    nom_fitxer = input("Introdueix el nom del fitxer: ")

    try:
        with open(nom_fitxer, 'r') as f:
            notes = [float(nota.replace(',', '.')) for nota in f.read().split() if nota != '-1']

        histograma = calcular_histograma(notes)
        nom_fitxer_sortida = f"{nom_fitxer[:-4]}-Histograma.txt"

        with open(nom_fitxer_sortida, 'w') as f:
            f.write(f"Histograma del fitxer {nom_fitxer}\n")
            f.write("-" * 30 + "\n")
            for nota, count in histograma.items():
                f.write(f"{nota}: {count}\n")

        print(f"S'ha creat l'histograma al fitxer {nom_fitxer_sortida}")

    except FileNotFoundError:
        print("Error: No s'ha trobat el fitxer.")
    except Exception as e:
        print("Error:", e)


def main():
    print("1. Exercici 1")
    print("2. Exercici 2")
    print("3. Exercici 3")
    opcio = input("Selecciona l'exercici (1/2/3): ")

    if opcio == '1':
        exercici1()
    elif opcio == '2':
        exercici2()
    elif opcio == '3':
        exercici3()
    else:
        print("Opció invàlida.")


if __name__ == "__main__":
    main()
