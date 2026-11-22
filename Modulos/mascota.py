
""" 
En este documento se va a hacer la clase Mascota, que se crea con código, código del cliente, 
nombre, tipo, raza, edad, tamaño, cuidados y visitas. Tiene el método agregar_servicio(nombre, precio), 
el método calcular_descuento(), que devuelve 0, 0.10, 0.15 o 0.35 según las visitas, y el método a_diccionario(). 
También hay una función suelta que crea la mascota desde un diccionario. Se conecta con el diagrama como el registro 
de la mascota (opción 1) y los rombos de descuento de “Salida y pago” (opción 4). Es la clase obligatoria del proyecto y 
debe usarse en esas dos partes.



"""
class Mascota:
    def __init__(
            self,
            codigo,
            codigo_cliente,
            nombre,
            tipo,
            raza,
            edad,
            tamanio,
            cuidados,
            visitas,):
        self.codigo = codigo
        self.codigo_cliente = codigo_cliente
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.edad = edad
        self.tamanio = tamanio
        self.cuidados = cuidados
        self.visitas = visitas
        self.servicios = []
           
        
    def agregar_servicio(self, nombre, precio):
        if precio <0:
            print("El precio del servicio no puede ser negativo")
        else:
            servicio = {
            "nombre": nombre,
            "precio": precio,
            }
            self.servicios.append(servicio)

    def calcular_descuento(self):
        if self.visitas < 3:
            descuento = 0
        elif self.visitas >= 3:
            descuento = 0.10
        elif self.visitas >= 5:
            descuento = 0.15
        else:
            descuento = 0.35 
        return descuento
    
    def diccionario(self):
        datos = {
            "codigo": self.codigo,
            "codigo_cliente": self.codigo_cliente,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "raza": self.raza,
            "edad": self.edad,
            "tamanio": self.tamanio,
            "cuidados": self.cuidados,
            "visitas": self.visitas,
            "servicios": self.servicios,
        }
        return datos

def creacion_mascota_diccionario(datos):
    mascota = Mascota(
        datos["codigo"],
        datos["codigo_cliente"],
        datos["nombre"],
        datos["tipo"],
        datos["raza"],
        datos["edad"],
        datos["tamanio"],
        datos["cuidados"],
        datos["visitas"],
    )
    if "servicios" in datos:
        for servicio in datos["servicios"]:
            mascota.agregar_servicio(servicio["nombre"], servicio["precio"])
    return mascota




#Asignado = "Fátima"

