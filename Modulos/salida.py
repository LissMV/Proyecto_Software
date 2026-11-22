from Modulos.validaciones import pedir_texto
from Modulos.mascota import creacion_mascota_diccionario
from Modulos.hospedaje import liberar_habitacion
from Modulos.servicios import calcular_total_servicios
from Modulos.cobro import calcular_total, calcular_cambio, generar_factura


def pedir_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))
        except ValueError:
            print("Debe escribir un número, por ejemplo 25 o 25.50.")
            continue

        if monto < 0:
            print("El monto no puede ser negativo.")
        else:
            return monto


def procesar_salida(datos):
    print("\n--- SALIDA Y PAGO ---")
    codigo = pedir_texto("Código de la mascota: ").upper()

    # 1. Validar que exista y esté hospedada
    if codigo not in datos["mascotas"]:
        print("Este código de mascota no es válido o no está registrado.")
        return

    datos_mascota = datos["mascotas"][codigo]
    estancia = datos_mascota.get("estancia")
    if estancia is None:
        print("Esta mascota no está hospedada actualmente.")
        return

    cliente = datos["clientes"][datos_mascota["codigo_cliente"]]
    habitacion = datos["habitaciones"][estancia["habitacion"]]

    # 2. Calcular
    subtotal_noches = habitacion["precio"] * estancia["noches"]
    subtotal_servicios = calcular_total_servicios(datos_mascota["servicios"])

    mascota = creacion_mascota_diccionario(datos_mascota)
    porcentaje = mascota.calcular_descuento()

    total = calcular_total(subtotal_noches, subtotal_servicios, porcentaje)
    desglose = {
        "subtotal_noches": subtotal_noches,
        "subtotal_servicios": subtotal_servicios,
        "descuento": porcentaje,
        "total": total,
    }

    # 3. Mostrar la factura
    print(generar_factura(cliente, datos_mascota, estancia, desglose))

    # 4. Cobrar (si cancela, no se modifica nada)
    pagado = False
    while not pagado:
        monto = pedir_monto("Monto recibido (0 para cancelar): ")
        if monto == 0:
            print("Salida cancelada. No se modificó nada.")
            return
        cambio = calcular_cambio(total, monto)
        if cambio == -1:
            print("El monto no alcanza para cubrir el total.")
        else:
            pagado = True
    print(f"Cambio: ${cambio}")

    # 5. Actualizar datos (solo con el pago confirmado)
    liberar_habitacion(datos, codigo)

    factor = 1 - porcentaje
    datos["ingresos"]["hospedaje"] = datos["ingresos"]["hospedaje"] + subtotal_noches * factor
    datos["ingresos"]["servicios"] = datos["ingresos"]["servicios"] + subtotal_servicios * factor

    for servicio in datos_mascota["servicios"]:
        nombre = servicio["nombre"]
        if nombre in datos["conteo_servicios"]:
            datos["conteo_servicios"][nombre] = datos["conteo_servicios"][nombre] + 1
        else:
            datos["conteo_servicios"][nombre] = 1

    datos_mascota["visitas"] = datos_mascota["visitas"] + 1
    datos_mascota["servicios"] = []
    datos_mascota["estancia"] = None
    print("Salida registrada. ¡Gracias por confiar en nosotros!")