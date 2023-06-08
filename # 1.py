# 1 
print("Ej1")
nombre = input("Introduzca su nombre:")
edad = input("Introduzca su edad: ")
print("Hola, {}. Tienes {} años.".format(nombre, edad))

#2 
print("Ej2")
Num1 = int(input("Introduzca un número: "))
Num2 = int(input("Introduzca un segundo número: "))
print(Num1, type(Num1), Num2, type(Num2))

#3 
print("Ej3")
I3 = int(input("Introduzca un número: "))
print(float(I3))

#4 
print("Ej4")
I4a = int(input("Introduzca un número: "))
I4b = int(input("Introduzca un segundo número: "))
print("Suma: ", I4a + I4b)
print("Resta", I4a - I4b)
print("Multiplicación", I4a * I4b)
print("División", I4a / I4b)
print("División Entera", I4a // I4b)
print("Módulo", I4a % I4b)
print("Potencia", I4a ** I4b)

#5
print("Ej5")
I5 = int(input("Ingrese un número: "))
print(I5 ** 0.5)

#6 
print("Ej6")
I6 = int(input("Ingrese un número: " ))
if I6 % 2 == 0: 
    print("Es par")
else: 
    print("Es Impar")

#7 
print("Ej7")
altura = float(input("Ingrese altura en: "))
peso = float(input("Ingrese peso: "))
print("Su IMC es: ", peso / (altura**2)) 

#8 
print("Ej8")
altura = float(input("Ingrese altura: "))
base = float(input("Ingrese base: "))
print("La superficie del triángulo es: ", (base * altura) /2 ) 

#9 
print("EJ9")
cantidad = float(input("Ingrese cantidad: "))
interes = float(input("Ingrese interes anual: "))
años = int(input("Ingrese años: "))

interes_decimal = interes / 100 
capital = cantidad * (1 + interes_decimal) ** años
print("El capital es de: ", capital)

#10
print("EJ10")
c_pa = int(input("Ingrese cantidad de payasos: "))
c_mu = int(input("Ingrese cantidad de muñecas: "))
peso_total = ((c_pa* 0.250) + (c_mu * 0.120))
print(peso_total)

#11
print("EJ11")

#12
print("EJ12")

#13
print("EJ13")
ent = int(input("Ingrese int: "))
flt = float(input("Ingrese un float: "))
boolean = bool(input("Ingrese True o False: "))
print("Entero: Tipo: {}, ID: {}, Valor: {}", format(type(ent), id(ent), ent))
print("Float: Tipo: {}, ID: {}, Valor: {}", format(type(flt), id(flt), flt))
print("Bool: Tipo: {}, ID: {}, Valor: {}", format(type(boolean), id(boolean), boolean))

#14
print("EJ14")
ent14 = int(input("Ingrese int: "))
flt14 = float(input("Ingrese un float: "))
boolean14 = bool(input("Ingrese True o False: "))
print("El valor cuando se convierte a int: {} ", format(int(ent14)))