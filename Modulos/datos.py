from Modulos.constantes import precios_habitacion, servicios


def crear_datos_iniciales():
    # Cuántas habitaciones hay de cada tipo (se puede cambiar aquí)
    cantidades = {"pequeno": 3, "mediano": 3, "grande": 2, "vip": 1}
    letras = {"pequeno": "P", "mediano": "M", "grande": "G", "vip": "V"}

    habitaciones = {}
    for tipo in cantidades:
        for numero in range(1, cantidades[tipo] + 1):
            codigo = letras[tipo] + str(numero)      # P1, P2, M1, ...
            habitaciones[codigo] = {
                "tipo": tipo,
                "precio": precios_habitacion[tipo],
                "ocupada": False,
                "mascota": None,
            }

    # Contador de cada servicio, todos empiezan en 0
    conteo_servicios = {}
    for nombre in servicios:
        conteo_servicios[nombre] = 0

    datos = {
        "clientes": {},
        "mascotas": {},
        "habitaciones": habitaciones,
        "ingresos": {"hospedaje": 0, "servicios": 0},
        "conteo_servicios": conteo_servicios,
        "contador_clientes": 0,
        "contador_mascotas": 0,
    }
    return datos