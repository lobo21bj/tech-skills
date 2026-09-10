# Usando llaves {}
mi_conjunto = {1, 2, 3, 4, 4} # El 4 duplicado se ignora
print(mi_conjunto) # Salida: {1, 2, 3, 4}

# Usando la función set() con un iterable
mi_lista = [1, 2, 2, 3]
otro_conjunto = set(mi_lista)
print(otro_conjunto) # Salida: {1, 2, 3}

# Para un conjunto vacío, usa set() no {} ({} crea un diccionario vacío)
conjunto_vacio = set()

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

#Metodos

frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()