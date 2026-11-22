
""" 
En este documento se van a hacer las funciones del registro: generar_codigo(prefijo, numero), registrar_dueno(datos), registrar_mascota(datos, codigo_cliente) y registrar(datos), que une todo. 
Se conecta con el diagrama como la opción 1 completa: “¿Ya está el dueño registrado?”, 
los datos del dueño y la mascota, el generar y vincular los códigos, 
y el mensaje de registro exitoso con ambos códigos.
Asignado = "Fabiola"
"""

from Modulos.validaciones import pedir_texto, pedir_entero, pedir_opcion, pedir_si_no
from Modulos.mascota import Mascota

def generar_codigo(prefijo, numero):
    if numero < 10:
      return prefijo + "00" + str(numero)
    elif numero < 100:
      return prefijo + "0" + str(numero)
    else:
      return prefijo + str(numero)

def registar_dueño(datos):
    print("\n--- Datos del dueño ---")
    nombre = pedir_texto("Nombre: ")
    telefono = pedir_texto("Telefono: ")
    direccion = pedir_texto("Direccion: ")
    
    datos["clientes"][codigo] = {
      "nombre": nombre,
      "telefono": telefono,
      "direccion": direccion,
      "mascota": []
    }
    return codigo

def registrar_mascota(datos, codigo_cliente):
    print("\n--- Datos de la mascota ---")
    nombre = pedir_texto("Nombre de la mascota: ")
    tipo = pedir_texto("Tipo de animal: ")
    raza = pedir_texto("Raza: ")
    edad = pedir_entero("Edad: ", 0, 30)
    tamaño = pedir_opcion("Tamaño (pequeño, mediano o grande): ", ["pequeño", "mediano", "grande"])
    
    if pedir_si_no("¿Necesita cuidados especiales? (s/n): "):
      cuidado = pedir_texto("¿Cuales?: ")
    else:
      cuidado = "Ninguno"

    datos["contador_mascotas"] = datos["contador_mascotas"] + 1
    codigo = generar_codigo("M", datos["contador_mascotas"])

    mascota = Mascota(codigo, codigo_cliente, nombre, tipo, raza, edad, tamano, cuidados, 0)
    datos["mascotas"][codigo] = mascota.a_diccionario()
    datos["clientes"][codigo_cliente]["mascotas"].append(codigo)
    return codigo

def registrar(datos):
    print("\n--- REGISTRO ---")
    if pedir_si_no("¿El dueño ya esta registrado? (s/n): ")
        codigo_cliente = pedir_texto("Codigo del dueño: ").upper()
        if codigo_cliente in datos["clientes"]:
            print("Dueño encontrado:", datos["clientes"][codigo_cliente]["nombre"])
        else:
            print("Ese codigo no existe. Vamos a registrar al dueño.")
            codigo_cliente = registrar_dueño(datos)
    else:
        codigo_cliente = registrar_dueño(datos)

    codigo_mascota = registrar_mascota(datos, codigo_cliente)
    print("\n¡Registro exitoso!")
    print("Codigo del dueño:", codigo_cliente)
    print("Codigo de la mascota:", codigo_mascota)
