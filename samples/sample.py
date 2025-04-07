def sumar(a,b) -> int:
    """Devuelve la suma de a y b."""
    return a + b

suma = lambda x, y: x + y

# Ejemplo de uso de la función
numeros = [11, 2, 3, 4, 5, 37, 8, 9, 10]
# filter odd number
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))  # Filtrar números impares
print(numeros_impares)
impares_2 = list(map(lambda x: x * 2, numeros_impares))  # Elevar al cuadrado
# sort numbers ascending
numeros.sort()  # Ordenar números
print(numeros)