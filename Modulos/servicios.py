""" 
En este documento se van a hacer tres funciones: 
mostrar_menu_servicios(), que imprime los servicios numerados con su precio; 
calcular_total_servicios(lista_servicios), que suma los precios y devuelve el total; y 
registrar_servicios(datos), que pide el código, pregunta cuántos servicios quiere y los guarda en la mascota. 
Se conecta con el diagrama como la opción 3, “Servicios extras”: 
el menú con los seis servicios, la cantidad a agregar y el cálculo de Precio_Servicios.
"""
from constantes import servicios

def mostrar_menu_servicios():
    print("--- Menú de servicios extras ---")
    numero = 1
    for nombre, precio in servicios.items():
        print(f"{numero}. {nombre} - ${precio}")
        numero = numero + 1

def calcular_total_servicios(lista_servicios):
    total = 0
    for servicio in lista_servicios:
        total = total + servicio["precio"]
    return total
#Esto viene de datos que solo esta como comenatario
def registrar_servicios(datos):
    mascotas = datos["mascotas"]
    codigo = input("Ingrese el código de la mascota: ")

    if codigo not in mascotas:
        print("No se encontró ninguna mascota con ese código")
        return

    mascota_indi = mascotas[codigo]
    #servicio viene también de datos que está como comentario
    if "servicios" not in mascota_indi:
        mascota_indi["servicios"] = []

    mostrar_menu_servicios()

    try:
        cantidad = int(input("¿Cuántos servicios extra desea agregar?: "))
    except ValueError:
        print("Ingrese un número entero válido, por favor")
        return

    lista_nombres = list(servicios.keys())

    for i in range(cantidad):
        try:
            opcion = int(input(f"Seleccione el número del servicio #{i + 1}: "))
        except ValueError:
            print("Entrada inválida. Ese servicio no se tomó en ceunta")
            continue

        if opcion >= 1 and opcion <= len(lista_nombres):
            nombre_servicio = lista_nombres[opcion - 1]
            precio_servicio = servicios[nombre_servicio]

            servicio = {
                "nombre": nombre_servicio,
                "precio": precio_servicio,
            }
            mascota_indi["servicios"].append(servicio)
            print(f"Servicio '{nombre_servicio}' agregado.")
        else:
            print("Opción inválida. Ese servicio no se agregó")

    print("Se finalizó con el proceso de registro de servicios ")

# Asignado = "Amy y Fátima"