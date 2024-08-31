# Definir la matriz 3x3 con valores numéricos
matriz = [
    [9, 7, 8],
    [3, 5, 1],
    [4, 6, 2]
]

# Función para ordenar una fila específica usando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambiar elementos
    return fila

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila_index):
    if fila_index < len(matriz):
        matriz[fila_index] = bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")
    return matriz

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
