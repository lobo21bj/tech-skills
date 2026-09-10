#Input de string
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

#Input de entero
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Output
nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")