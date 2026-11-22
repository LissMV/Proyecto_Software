"""
En este documento se van a hacer las funciones de habitaciones: calcular_costo_hospedaje(tipo, noches),
buscar_habitacion_libre(datos, tipo), liberar_habitacion(datos, codigo_mascota) y hospedar_mascota(datos),
que es la que llama el menú. Se conecta con el diagrama como la opción 2, “Hospedaje”: pedir noches y VIP,
decidir entre VIP, pequeño, mediano o grande, “¿Disponibilidad de este tipo de habitación?” y el mensaje
“Lamentamos informarle...”. Agrega lo que falta: marcar el cuarto como ocupado y liberarlo al salir.
Asignado = "Liss"
"""
from Modulos.constantes import precios_habitacion


def pedir_datos_estadia():
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


def det_tipo_habitacion(es_vip, tamano):
    if es_vip:
        return "vip"
    return tamano


def calcular_costo_hospedaje(tipo, noches):
    return precios_habitacion[tipo] * noches


def buscar_habitacion_libre(datos, tipo):
    for codigo in datos["habitaciones"]:
        habitacion = datos["habitaciones"][codigo]
        if habitacion["tipo"] == tipo and not habitacion["ocupada"]:
            return codigo
    return None


def liberar_habitacion(datos, codigo_mascota):
    estancia = datos["mascotas"][codigo_mascota]["estancia"]
    habitacion = datos["habitaciones"][estancia["habitacion"]]
    habitacion["ocupada"] = False
    habitacion["mascota"] = None


def hospedar_mascota(datos):
    print("\n--- HOSPEDAJE ---")
    codigo = input("Ingrese el código de la mascota registrada: ").strip().upper()

    if codigo not in datos["mascotas"]:
        print("Este código de mascota no es válido o no esta registrado")
        return

    mascota = datos["mascotas"][codigo]
    if mascota.get("estancia") is not None:
        print("Esta mascota ya está hospedada.")
        return

    noches, es_vip = pedir_datos_estadia()
    tipo = det_tipo_habitacion(es_vip, mascota["tamanio"])
    codigo_habitacion = buscar_habitacion_libre(datos, tipo)

    if codigo_habitacion is None:
        print("Lamentamos informar que la habitación seleccionada/asignada "
              "no esta disponible, intente en otro momento")
        return

    datos["habitaciones"][codigo_habitacion]["ocupada"] = True
    datos["habitaciones"][codigo_habitacion]["mascota"] = codigo
    mascota["estancia"] = {"habitacion": codigo_habitacion, "noches": noches}

    total = calcular_costo_hospedaje(tipo, noches)
    print(f"Habitación {codigo_habitacion} ({tipo}) por {noches} noche(s). Total de hospedaje: ${total}")