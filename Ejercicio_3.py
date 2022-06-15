#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

radio = float(input("Ingrese un valor para el radio de su circulo: "))
área = 3.14 * (radio**2)
resultado = área
print(f"El resultado del area de su circulo es {resultado} ")
altura = float(input("Ingrese la altura de su cilindro: "))
resultado = área * altura 
print(f"El el volumen del cilindro es: {resultado}")