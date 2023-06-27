#1
fruta_y_precio = {'Banana': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input('¿Qué fruta estás buscando?: ')
kilos = float(input("Ingrese el número de kilos: "))

if fruta in fruta_y_precio:
    fruta_y_precio = fruta_y_precio[fruta] * kilos
    print("El precio de", kilos, "kilos de", fruta, "es:", fruta_y_precio)
else:
    print("La fruta", fruta, "no está en el diccionario de precios.")

#2 
EC = {'Nombre': 'Emilia', 'Apellido': 'Cabrera', 'Edad': '23 años', 'Email': 'ecabrera@curso.com'}
GAP = {'Nombre': 'Gustavo Andrés', 'Apellido': 'Peralta', 'Edad': '26 años', 'Email': 'gperalta@curso.com'}

