"""   

En este documento se van a hacer las funciones de habitaciones: calcular_costo_hospedaje(tipo, noches), buscar_habitacion_libre(datos, tipo), asignar_habitacion(datos, codigo_mascota, noches, quiere_vip), liberar_habitacion(datos, codigo_mascota) y hospedar_mascota(datos), 
que es la que llama el menú.  Se conecta con el diagrama como la opción 2, “Hospedaje”: pedir noches y VIP, 
decidir entre VIP, pequeño, mediano o grande, “¿Disponibilidad de este tipo de habitación?” y el mensaje 
“Lamentamos informarle...”. 
Agrega lo que falta: marcar el cuarto como ocupado y liberarlo al salir.

"""

#COSTANTE# ---> Precio por noche según cada habitación.

TARIFAS = {
    "VIP": 28,
    "Grande": 18,
    "Mediano": 13,
    "Pequeño": 8,
}

#VARIABLES# ---> Cantidad de habitaciones disponibles.

habitaciones_disponibles = {
    "VIP": 4,
    "Grande": 5,
    "Mediano": 7,
    "pequeño": 8
}

#ENTRADAS#

def pedir_codigo_mascota():
    return input("Ingrese el código de la mascota registrada: ").strip()

def pedir_datos_estadia():
    #Pide cantidad de noches y si desea habitación VIP.
    while True:
        try:
            noches = int(input("Cantidad de noches: "))
            if noches > 0:
                break
            print("Debe ser un número mayor a 0.")
        except ValueError:
            print("Ingrese un número entero válido.")

    while True:
        respuesta = input("¿Desea habitación VIP? (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            break
        print("Responda 's' o 'n'.")

    return noches, respuesta == "s"

def calcular_costo_hospedaje():
    pass

