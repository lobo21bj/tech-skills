persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}