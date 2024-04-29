import logging
import time

# Configurar el registro de errores en un archivo
logging.basicConfig(filename='recorregut.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Simulando alguna operación
        resultado = 10 / 0  # Esto generará un error de división por cero
    except Exception as e:
        # Registrar el error en el archivo de registro
        logging.error(f"Error encontrado: {e}")

    # Simular alguna incidencia
    logging.info("Se encontró una incidencia: X ha ocurrido.")

if __name__ == "__main__":
    start_time = time.time()

    # Ejecutar el programa principal
    main()

    # Calcular el tiempo transcurrido
    elapsed_time = time.time() - start_time
    # Anotar el tiempo transcurrido en el archivo de registro
    logging.info(f"Tiempo transcurrido: {elapsed_time} segundos.")
