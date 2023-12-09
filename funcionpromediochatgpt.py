def calcular_promedio(datos):
    if len(datos) == 0:
        return 0  # Manejo de lista vacía para evitar la división por cero
    suma = sum(datos)
    promedio = suma / len(datos)
    return promedio
