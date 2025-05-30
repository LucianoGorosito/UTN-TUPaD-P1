# Trabajo Práctico 4

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num= int(input("Ingrese un número entero: "))
contador = 0
while num > 0:
    num = num // 10
    contador += 1
print("La cantidad de dígitos es:", contador)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0 
num = int(input("Ingrese un numero entrero, ingrese 0 para salir: "))
while num != 0:
    suma += num
    num = int(input("Ingrese un numero entrero, ingrese 0 para salir: "))
print("La suma total es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 
intentos = 0
num = random.randint(0,9)
while num in  range(0,10):
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == num:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    elif intento < num:
        print("El número es mayor.")
    else:
        print("El número es menor.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# # número entero positivo indicado por el usuario.

suma = 0 
num = int(input("Ingrese un número entero positivo: "))
for i in range(0, num + 1):
    suma += i
print("La suma de los números entre 0 y", num, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0 
positivos = 0 
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0 
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    suma += num
promedio = suma / 100
print("La media de los números ingresados es:", promedio)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número entero: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print("El número invertido es:", invertido) 