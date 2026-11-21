
""" 
En este documento se van a hacer las funciones del registro: generar_codigo(prefijo, numero), registrar_dueno(datos), registrar_mascota(datos, codigo_cliente) y registrar(datos), que une todo. 
Se conecta con el diagrama como la opción 1 completa: “¿Ya está el dueño registrado?”, 
los datos del dueño y la mascota, el generar y vincular los códigos, 
y el mensaje de registro exitoso con ambos códigos.
Asignado = "Fabiola"
"""

from Modulos.validaciones import pedir_texto, pedir_entero, pedir_opcion, pedir_si_no
from Modulo.mascota import Mascota

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

  datos[""]
