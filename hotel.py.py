from Modulos.datos import crear_datos_iniciales
from Modulos.persistencia import cargar_datos, guardar_datos
from Modulos.validaciones import pedir_opcion
from Modulos.registro import registrar
from Modulos.hospedaje import hospedar_mascota
from Modulos.servicios import registrar_servicios
from Modulos.salida import procesar_salida
from Modulos.reportes import mostrar_reporte


def mostrar_menu():
    print("\nBIENVENIDO AL HOTEL DE MASCOTAS")
    print("-------- Menú de opciones --------")
    print("1. Registro de dueños y mascotas")
    print("2. Hospedaje")
    print("3. Servicios extras")
    print("4. Salida y pago")
    print("5. Reporte del local")
    print("6. Salir")


def main():
    datos = cargar_datos(crear_datos_iniciales())

    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = pedir_opcion("Elija una opción (1-6): ", ["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            registrar(datos)
        elif opcion == "2":
            hospedar_mascota(datos)
        elif opcion == "3":
            registrar_servicios(datos)
        elif opcion == "4":
            procesar_salida(datos)
        elif opcion == "5":
            mostrar_reporte(datos)

        guardar_datos(datos)

    print("Datos guardados. ¡Hasta pronto!")


main()