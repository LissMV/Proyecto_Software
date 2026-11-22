
""" En este documento se va a hacer la función mostrar_reporte(datos), en pasos pequeños. Primero cuenta las mascotas registradas, 
luego los cuartos ocupados y libres con un for, después busca el servicio más solicitado y
por último muestra los ingresos por hospedaje, por servicios y el total. Se conecta con el diagrama como la opción 5, el reporte del local, con la lista de lo que se muestra: 
mascotas registradas, espacios disponibles y ocupados, servicios más solicitados y los tres ingresos."""

Asignado = "Gaby"


def contar_mascotas(datos):
    return len(datos["mascotas"])


def contar_habitaciones(datos):
    ocupadas = 0
    libres = 0
    for numero in datos["habitaciones"]:
        habitacion = datos["habitaciones"][numero]
        if habitacion["ocupada"]:
            ocupadas = ocupadas + 1
        else:
            libres = libres + 1
    return ocupadas, libres


def buscar_servicios_mas_solicitados(datos):
    conteo = datos["conteo_servicios"]
    mayor = 0
    for servicio in conteo:
        if conteo[servicio] > mayor:
            mayor = conteo[servicio]

    if mayor == 0:
        return [], 0

    mas_pedidos = []
    for servicio in conteo:
        if conteo[servicio] == mayor:
            mas_pedidos.append(servicio)
    return mas_pedidos, mayor


def mostrar_reporte(datos):
    cantidad_mascotas = contar_mascotas(datos)
    ocupadas, libres = contar_habitaciones(datos)
    mas_pedidos, veces = buscar_servicios_mas_solicitados(datos)


    ingreso_hospedaje = datos["ingresos"]["hospedaje"]
    ingreso_servicios = datos["ingresos"]["servicios"]
    ingreso_total = ingreso_hospedaje + ingreso_servicios

    print("\n========== REPORTE DEL LOCAL ==========")
    print("Mascotas registradas:", cantidad_mascotas)
    print("Habitaciones ocupadas:", ocupadas)
    print("Habitaciones disponibles:", libres)

    if len(mas_pedidos) == 0:
        print("Servicio más solicitado: todavía no se ha pedido ninguno.")
    elif len(mas_pedidos) == 1:
        print("Servicio más solicitado:", mas_pedidos[0], "(" + str(veces) + " veces)")
    else:
        print("Servicios más solicitados (empate con " + str(veces) + " veces cada uno):")
        for servicio in mas_pedidos:
            print("  -", servicio)

    print("Ingreso por hospedaje: $" + format(ingreso_hospedaje, ".2f"))
    print("Ingreso por servicios: $" + format(ingreso_servicios, ".2f"))
    print("Ingresos totales:      $" + format(ingreso_total, ".2f"))
    print("=======================================")


# Prueba rápida: solo corre si ejecutas este archivo directamente

if __name__ == "__main__":
    datos_prueba = {
        "mascotas": {"M001": {}, "M002": {}, "M003": {}},
        "habitaciones": {
            "P1": {"tipo": "pequeno", "precio": 8, "ocupada": True, "mascota": "M001"},
            "P2": {"tipo": "pequeno", "precio": 8, "ocupada": False, "mascota": None},
            "M1": {"tipo": "mediano", "precio": 13, "ocupada": True, "mascota": "M002"},
            "V1": {"tipo": "vip", "precio": 28, "ocupada": False, "mascota": None},
        },
        "conteo_servicios": {"Baño": 3, "Paseo": 3, "Corte de pelo": 1},
        "ingresos": {"hospedaje": 120, "servicios": 54},
    }
    mostrar_reporte(datos_prueba)