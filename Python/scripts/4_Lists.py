cortes = ["Asado", "Vacío", "Lomo", "Matambre"]

print(cortes[0]) #imprime Asado
print(cortes[1]) #imprime Vacío
print(cortes[2]) #imprime Lomo
print(cortes[3]) #imprime Matambre

#Reverse
print(cortes[-1]) #imprime Matambre
print(cortes[-2]) #imprime Lomo
print(cortes[-3]) #imprime Vacío
print(cortes[-4]) #imprime Asado

#Append
cortes.append("Entraña")
print(cortes)

#Insert
cortes.insert(0, "Molleja")
print(cortes)

#Remove
cortes.remove("Molleja")
print(cortes)

#Pop -Extraer
corte_eliminado = cortes.pop(4)
print(cortes)
print(corte_eliminado)

#Sort
cortes.sort()
print(cortes)

#Reverse sort
cortes.reverse()
print(cortes)