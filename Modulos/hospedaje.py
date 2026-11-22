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
    "grande": 18,
    "mediano": 13,
    "pequeño": 8,
}

#VARIABLES# ---> Cantidad de habitaciones disponibles.

habitaciones_disponibles = {
    "VIP": 4,
    "grande": 5,
    "mediano": 7,
    "pequeño": 8
}

def obtener_tamano_mascota(codigo):
    mascotas_demo = {"M001": "Pequeño", "M002": "Mediano", "M003": "Grande"}
    return mascotas_demo.get(codigo)

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

#LÓGICA#

def validar_codigo(codigo):
    return obtener_tamano_mascota(codigo) is not None

def det_tipo_habitacion(es_vip, tamaño):
    if es_vip:
        return "VIP"
    return tamaño.strip().lower()

def disponibilidad(tipo_habitacion):
    return habitaciones_disponibles.get(tipo_habitacion, 0) > 0

def calcular_precio(tipo_habitacion, noches):
    return TARIFAS[tipo_habitacion] * noches

#Funciones que se van a mandar a llamar en el main/cuerpo.

def hospedaje():
    codigo = pedir_codigo_mascota()
    
    if not validar_codigo(codigo):
        print("Este código de mascota no es válido o no esta registrado")
        raise TypeError("Invalido")
    
    tamaño = obtener_tamano_mascota(codigo)
    noches, es_vip = pedir_datos_estadia()
    
    tipo = det_tipo_habitacion(es_vip, tamaño)
    
    if not disponibilidad(tipo):
        print("Lamentamos informar que la habitación seleccionada/asignada "
        "no esta disponible, intente en otro momento")
        return None
    
    total = calcular_precio(tipo, noches)
    print(f"Habitación {tipo} por {noches} noche(s). Total a pagar: ${total}")
    
    return total

if __name__ == "__main__":
    hospedaje()
        
    