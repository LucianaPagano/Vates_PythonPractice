#Tarea 2

#1 
print("Ej 1")
nombre = str(input("¿Cual es tu nombre?: "))
loop = int(input("Decime un número: "))
for i in range(loop): 
    print(nombre)

#2 
print("Ej 2")
nombre = str(input("¿Cual es tu nombre?: "))
apellido = str(input("¿Cual es tu apellido?: "))
print(" {}, {}".format(apellido, nombre)) 

#3 
print("Ej 3")
samba = input("Ingrese nombre de ruta remota: ")
if samba.startswith('//'):
    samba[2:]
nombre, ruta = samba.split('/', 1)
print("Host: {}, Ruta: {}".format(nombre, ruta))

#4 
print("Ej 4")
correo = input("Agrege correo: ")
nombre, handle = correo.split("@", 1)
print(nombre + "@educ.ar")

#5 
print("Ej 5")
DNI = int(input("Ingrese DNI: "))
if DNI % 23 == 0: 
    print("{}T".format(DNI))
elif DNI % 23 == 1: 
    print(DNI, "R")
elif dni % 23 == 2: 
    print(DNI, "W")
elif dni % 23 == 3: 
    print(DNI, "A")
elif dni % 23 == 4: 
    print(DNI, "G")
elif dni % 23 == 5: 
    print(DNI, "M")
elif dni % 23 == 6: 
    print(DNI, "Y")
elif dni % 23 == 7: 
    print(DNI, "F")
elif dni % 23 == 8: 
    print(DNI, "P")
elif dni % 23 == 9: 
    print(DNI, "D")
elif dni % 23 == 10: 
    print(DNI, "X")
elif dni % 23 == 11: 
    print(DNI, "B")
elif dni % 23 == 12: 
    print(DNI, "N")
elif dni % 23 == 13: 
    print(DNI, "J")
elif dni % 23 == 14: 
    print(DNI, "Z")
elif dni % 23 == 15: 
    print(DNI, "S")
elif dni % 23 == 16: 
    print(DNI, "Q")
elif dni % 23 == 17: 
    print(DNI, "V")
elif dni % 23 == 18: 
    print(DNI, "H")
elif dni % 23 == 19: 
    print(DNI, "L")
elif dni % 23 == 20: 
    print(DNI, "C")
elif dni % 23 == 21: 
    print(DNI, "K")
elif dni % 23 == 22: 
    print(DNI, "E")

print("Ej 5")
dni = int(input("Ingrese DNI: "))
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
indice = dni % 23

if indice == 0: 
    print("{}T".format(dni))
else:
    letra_dni = letras[indice]
    print("{}{}".format(dni, letra_dni))
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
#3 
print("Ej 3")
