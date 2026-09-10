cortes = ["Asado", "Vacío", "Lomo", "Matambre"]

print("Estos son los cortes de Carne seleccionados:")
for corte in cortes:
    print(corte)

contador = 0

print("\nPrueba de contador:")
while contador < 5:
    print(contador)
    contador += 1

contador = 0

print("\nContador con break:")
while True:
    print(contador)
    contador += 1

    if contador == 5:
        break
print("Salí del loop porque llegué a 5!")

print("\nContador con continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("\nContador con pass (reserva bloque de memoria):")
for j in range(5):
    pass