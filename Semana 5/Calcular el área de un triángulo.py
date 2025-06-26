# Programa para calcular el área de un triángulo
# Este programa solicita al usuario ingresar la base y la altura de un triángulo,
# luego calcula y muestra el área correspondiente.

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Solicitar al usuario la base y la altura
base_ingresada = float(input("Ingrese la base del triángulo en cm: "))
altura_ingresada = float(input("Ingrese la altura del triángulo en cm: "))

# Validación simple para asegurar que los datos sean positivos
datos_validos = base_ingresada > 0 and altura_ingresada > 0

if datos_validos:
    # Calcular el área utilizando la función
    area_triangulo = calcular_area_triangulo(base_ingresada, altura_ingresada)
    print(f"El área del triángulo es: {area_triangulo} cm²")
else:
    print("Error: La base y la altura deben ser números positivos.")
