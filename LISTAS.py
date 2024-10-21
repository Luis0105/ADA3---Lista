from collections import deque

lista = deque()

lista.append("Palabra")
lista.append(5)
lista.append(17)
lista.append("Palabra 2")

lista.pop()

print("El tamaño de la lista es:", len(lista))
print(lista[-1])
