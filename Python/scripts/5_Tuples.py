mi_tupla = (1, 2, 3, 2, 4, 2)

#index(value) --> Output is Index key
print (mi_tupla.index(2)) # Searches for value 2 - Output: 1
print (mi_tupla.index(2, 2)) # Searches for value 2 from position 2 onwards - Output: 3
print (mi_tupla.index(2, 2, 4)) # Searches for value 2 from position 2 to 4 - Output: 3