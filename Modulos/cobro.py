"""
En este documento se van a hacer los cálculos del pago:
calcular_total(subtotal_noches, subtotal_servicios, porcentaje_descuento),
calcular_cambio(total, monto_recibido) y generar_factura(cliente, mascota, estancia, desglose).
Esta última devuelve el texto de la factura y no imprime nada.
Se conecta con el diagrama como los bloques de “precio final = Precio_Servicios + Precio_noche − descuento” de la opción
4. Agrega la factura, que aún no está en el diagrama.
Asignado = "Fabiola"
"""
def calcular_total(subtotal_noches, subtotal_servicios, porcentaje_descuento):
    subtotal = subtotal_noches + subtotal_servicios
    descuento = subtotal * porcentaje_descuento
    total = subtotal - descuento
    return round(total, 2)

def calcular_cambio(total, monto_recibido):
    if monto_recibido < total:
        return -1
    return round(monto_recibido - total, 2)

def generar_factura(cliente, mascota, estancia, desglose):
    subtotal = desglose["subtotal_noches"] + desglose["subtotal_servicios"]
    monto_descuento = round(subtotal * desglose["descuento"], 2)
    porcentaje = int(desglose["descuento"] * 100)

    factura = "---------- FACTURA ----------\n"
    factura += f"Dueño: {cliente['nombre']}\n"
    factura += f"Mascota: {mascota['nombre']}\n"
    factura += f"Habitación: {estancia['habitacion']}\n"
    factura += f"Noches: {estancia['noches']}\n"

    factura += "Servicios realizados:\n"
    if len(mascota["servicios"]) == 0:
        factura += "  (ninguno)\n"
    for servicio in mascota["servicios"]:
        factura += f"  - {servicio['nombre']}: ${servicio['precio']}\n"
    factura += f"Hospedaje: ${desglose['subtotal_noches']}\n"
    factura += f"Servicios: ${desglose['subtotal_servicios']}\n"
    factura += f"Subtotal: ${subtotal}\n"
    factura += f"Descuento ({porcentaje}%): -${monto_descuento}\n"
    factura += f"TOTAL: ${desglose['total']}\n"
    factura += "-----------------------------"
    return factura