# Programa para calcular el promedio semanal del clima

def ingresar_temperatura():
    """Solicita al usuario ingresar las temperaturas de los 7 días"""
    temperaturas = []
    for día in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {día}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas"""
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """Muestra el resultado del promedio semanal"""
    print(f"El promedio semanal de temperatura es: {promedio:.2f} ºC")

# Ejecución del programa
def main():
    temperaturas = ingresar_temperatura()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

# Llamada al programa principal
if __name__ == "__main__":
    main()

