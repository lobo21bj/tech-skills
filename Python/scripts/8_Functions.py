#Valores de Retorno
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7

#Funciones que imprimen strings
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

#Funciones lambda, definidas en la misma linea
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

#Variables locales y globales
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
try:
    print(variable_local)  # Genera un error, la variable no está definida en este alcance.
except NameError:
    print("variable_local no existe")

#Funciones con nro variable de argumentos
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22