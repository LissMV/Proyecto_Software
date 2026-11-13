#Clase para guardar mis clientes (dueños de mascotas)
class Cliente:
    def __init__(self, name:str, phone:str, address:str ):
        self.name = name
        self.phone = phone
        self.address = address
        self.pets = []
        self.code = []
    
#Esta función agregará las mascotas dentro de la clase Cliente, especificamente en self.pets = []
    def agregar_mascota(self, mascota):
        self.pets.append(mascota)
        
#Clase para guardar las mascotas
class Mascota:
    def __init__(self, name:str, pet_type:str, race:str, years:int):
        self.name = name
        self.pet_type = pet_type
        self.race = race
        self.years = years
        self.special_care = []
    

        
        
