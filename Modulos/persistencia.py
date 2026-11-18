"""  

En este documento se va a hacer guardar el diccionario 
datos en un archivo y volver a cargarlo al abrir el programa. 
Se conecta con el diagrama como el paso final de cada operación (guardar) y 
el inicio del programa (cargar). Es lo último que se agrega y 
debe usar la forma que enseñe el docente. Mientras tanto, esta es una opción en JSON:


import json
import os

RUTA_ARCHIVO = "datos/hotel_datos.json"


def guardar_datos(datos, ruta=RUTA_ARCHIVO):
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"No se pudo guardar el archivo: {error}")
        return False


def cargar_datos(datos_por_defecto, ruta=RUTA_ARCHIVO):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Todavía no hay datos guardados. Se empieza desde cero.")
        return datos_por_defecto
    except json.JSONDecodeError:
        print("El archivo de datos está dañado. Se empieza desde cero.")
        return datos_por_defecto
        
        
    Código hecho 100% por IA es de q revisar y preguntar a Alvin si no se entiende como algo 
    funciona
"""

Asignado = "Liss"