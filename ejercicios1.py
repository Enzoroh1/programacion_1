#ejemplo 1
base = int(input("ingrese el valor de la base "))
altura = int(input("ingrese el valor de altura "))
print("el area del rectangulo es", base * altura)

base = int(input("ingrese el valor de la base "))
altura = int(input("ingrese el valor de altura "))
area = base * altura
print("el area del rectangulo es", area, "cm")

base = float(input("ingrese el valor de la base "))
altura = float(input("ingrese el valor de altura "))
area = base * altura
print("el area del rectangulo es", round(area, 2), "cm")
#(round redondea el valor decimal, ej: 2.56 cm)

#ejemplo 2
valor_maquina = int(input("valor de la maquina "))
valor_dolar = int(input("valor del dolar "))
print("el valor en pesos de la maquina es ", valor_dolar * valor_maquina)
#puede ser float para numeros con coma o int para numeros enteros

#ejemplo 3
anio_edad = int(input("ingrese año de nacimiento "))
anio_actual = int(input("ingrese año actual "))
print("la edad es", anio_edad - anio_actual, "años")

anio_nacimiento = int(input("ingrese año de nacimiento"))
print("tiene", 2021 - anio_nacimiento, "años")

#ejemplo 4
base = int(input("ingrese base del triangulo: "))
altura = int(input("ingrese altura del triangulo: "))
print("la base del triangulo es", base * altura)

#ejemplo 5
horas_cliente = int(input("ingrese cantidad de horas "))
print("debe pagar $", 10 * horas_cliente)

#ejemplo 6
cantidad_m2 = int(input("ingrese la cantidad de m2 a pintar"))
costo_litro_pintura = float(input("costo del litro de pintura"))
total_pintura = cantidad_m2 * costo_litro_pintura
mano_obra = total_pintura * 0.45
total = total_pintura * mano_obra
print("el monto total es", total)

#ejemplo 7
from math import sqrt #libreria importada
lado_a = int(input("ingrese lado a "))
lado_b = int(input("ingrese lado b "))
diagonal = sqrt(lado_a ** 2 * lado_b ** 2)
print("la distancia en diagonal es", diagonal, "m2")

from math import sqrt #libreria importada
lado_a = int(input("ingrese lado a "))
lado_b = int(input("ingrese lado b "))
diagonal = round(sqrt(lado_a ** 2 * lado_b ** 2)) #redondeo
print("la distancia en diagonal es", diagonal, "m2")

from math import sqrt #libreria importada
lado_a = int(input("ingrese lado a "))
lado_b = int(input("ingrese lado b "))
diagonal = int(sqrt(lado_a ** 2 + lado_b ** 2)) #numero entero
print("la distancia en diagonal es", diagonal, "m

#ejemplo 8
tiro_aro = int(input("ingrese la cantidad de tiros realizados "))
tiro_acertado = int(input("ingrese tiros acertados "))
eficencia = tiro_acertado * 100 // tiro_aro
print ("la eficiencia es del", eficencia,"%")

#ejercicio 9
kilomtros_recorridos = int(input("ingresa los kilomtros recorrido"))
total = kilomtros_recorridos * 100 #el valor del kilomtro
print("el costo del viajes es $", total)

#ejercicio 10
kilometros = int(input("ingrese los kilometros realizados "))
ecuacion = kilometros * 1
print("va a tardar", ecuacion, "horas")

#ejercicio 11
minutos = int(input("ingrese duracion de llamada en minutos"))
costo_minuto = int(input("ingrese costo del minuto de llamda"))
total_llamadas = minutos * costo_minuto
adicional = 5 * total_llamadas / 100
total = total_llamadas * adicional
print(total)

#ejercicio 12
