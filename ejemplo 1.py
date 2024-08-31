# Definir la matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j  # Retorna la posición si se encuentra el valor
    return None  # Retorna None si no se encuentra el valor

# Valor que se desea buscar
valor_buscado = 5

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado de la búsqueda
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion} de la matriz.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
