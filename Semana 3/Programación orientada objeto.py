# Programa POO para calcular el promedio semanal del clima

class ClimaDiario:
    def __init__(self):
        # Lista privada para almacenar las temperaturas
        self.__temperaturas = []

    def ingresar_temperatura(self):
        """Método para ingresar temperaturas por día"""
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas"""
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultado(self):
        """Método para mostrar el resultado"""
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} ºC")

# Clase hija para extender funcionalidad
class ClimaExtendido(ClimaDiario):
    def mostrar_mensaje(self):
        print("Calculando el promedio semanal del clima usando POO...")

# Ejecución del programa
def main():
    clima = ClimaExtendido()
    clima.mostrar_mensaje()
    clima.ingresar_temperatura()
    clima.mostrar_resultado()

if __name__ == "__main__":
    main()
