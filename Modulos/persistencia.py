"""
En este documento se va a hacer guardar el diccionario datos en un archivo
y volver a cargarlo al abrir el programa. Se conecta con el diagrama como el
paso final de cada operación (guardar) y el inicio del programa (cargar).
Es lo último que se agrega y debe usar la forma que enseñe el docente.
Asignado = "Liss"
"""
import json

RUTA_ARCHIVO = "hotel_datos.json"


def guardar_datos(datos):
    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print("No se pudo guardar el archivo de datos.")


def cargar_datos(datos_por_defecto):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Todavía no hay datos guardados. Se empieza desde cero.")
        return datos_por_defecto
    except json.JSONDecodeError:
        print("El archivo de datos está dañado. Se empieza desde cero.")
        return datos_por_defecto