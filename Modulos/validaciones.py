""" 


En este documento se van a hacer funciones que piden un dato y no dejan avanzar hasta que sea válido: 
pedir_texto(mensaje), pedir_entero(mensaje, minimo, maximo), pedir_opcion(mensaje, opciones_validas) y pedir_si_no(mensaje). 
Se conecta con el diagrama como todos los rombos de “¿Datos válidos?”, “¿Código válido?” y “¿Opción entre 1 y 6?”, incluidos los “TypeError: Inválido”. 
En lugar de repetir esas comprobaciones en cada módulo, todos usan estas funciones.

"""
Asignado = "Fátima"
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Entrada inválida. El texto no puede estar vacío.")
        else:
            return texto

def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
            continue

        if numero < minimo or numero > maximo:
            print(f"El número debe estar entre {minimo} y {maximo}.")
        else:
            return numero

def pedir_opcion(mensaje, opciones_validas):
    opciones_limpias = []
    for op in opciones_validas:
        opciones_limpias.append(str(op).strip().lower())

    while True:
        eleccion = input(mensaje).strip().lower()

        if eleccion in opciones_limpias:
            return eleccion
        else:
            print("Opción inválida, inténtelo de nuevo.")

def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta in ["s", "si", "sí"]:
            return True
        elif respuesta in ["n", "no"]:
            return False
        else:
            print("Respuesta inválida. Por favor escriba 's' o 'n'.")