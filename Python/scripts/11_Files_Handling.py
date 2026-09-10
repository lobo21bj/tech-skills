#File read
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#File write
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

#File read with closure
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)