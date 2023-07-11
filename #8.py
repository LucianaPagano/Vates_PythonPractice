#1
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def print_nombre(self):
        print("Nombre del estudiante:", self.nombre)

estudiante1 = Estudiante("Luciana")

estudiante1.print_nombre()
#2 
class Rectangulo: 
    def __init__(self, largo, ancho): 
        self.largo = largo  
        self.ancho = ancho 

    def valor_area(self): 
        area = self.largo * self.ancho
        return area 

area_rect = Rectangulo(5, 9) 
area_rectangulo1 = area_rect.valor_area()
print("El área del rectángulo es:", area_rect)
#3 
class Circulo: 
    def __init__(self, radio): 
        self.radio
    
    def set_radio(self):
        
    def get_area(self): 
        
