# Ejercicio 1
print("Hola Mundo")
# Ejercicio 2 
nom = input("Ingrese su nombre: ")
print(f"Hola {nom}")
# Ejercicio 3 
nom= input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: " )
print(f"Su nombre es {nom}, su edad es {edad} y su lugar de residencia es {residencia}")
# Ejercicio 4
radio = input("Ingrese el radio de un circulo: ")
area = 3.14 * (float(radio) ** 2)
perimetro = 3.14 * (float(radio) * 2)
print(f"El area del circulo es {area} y su perimetro es {perimetro}")
# Ejercicio 5
segundos = input("Ingrese la cantidad de segundos: ")
horas = int(segundos) / 3600
print(f"La cantidad de segundos ingresados equivale a {horas} horas")
# Ejercicio 6
num = input("Ingrese un numero: ")
for i in range(1, 11):
    print(f"{num} x {i} = {int(num) * i}")
# Ejercicio 7
num1 = int(input("Ingrese un numero distinto de 0: "))
num2 = int(input("Ingrese otro numero distinto de 0: "))
if num1 and num2 != 0:
    suma= (num1+num2)
    resta = (num1-num2)
    multiplicacion = (num1 * num2)
    division = (num1 / num2)
    print(f"La suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion} y la division es {division}") 
else :
    print("No se puede realizar la operacion")
# Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print (f"Su indice de masa corporal es {imc}")
# Ejercicio 9 
temp = int(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (temp * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es {fahrenheit}")
# Ejercicio 10 
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))
promedio = (num1+num2+num3)/3
print(f"El promedio de los tres numeros ingresados es {promedio}")
