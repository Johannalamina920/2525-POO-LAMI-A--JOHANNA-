# Programa de ejemplo sobre Vehículos

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"{self.__class__.__name__} - Marca: {self.marca}, Modelo: {self.modelo}")

    def conducir(self):
        print("Conduciendo un vehículo.")

# Clase derivada que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas  # Atributo privado

    # Encapsulamiento moderno con property
    @property
    def puertas(self):
        return self.__puertas

    @puertas.setter
    def puertas(self, valor):
        if valor > 0:
            self.__puertas = valor
        else:
            print("El número de puertas debe ser mayor a 0.")

    # Polimorfismo: sobrescritura del sistema de conducir
    def conducir(self):
        print(f"Conduciendo un auto {self.marca} {self.modelo} con {self.__puertas} puertas.")

# Otra clase derivada para mostrar polimorfismo
class Moto(Vehiculo):
    def conducir(self):
        print(f"Conduciendo una moto {self.marca} {self.modelo}.")

# Crear objetos (instancias) de las clases
vehiculo1 = Vehiculo("Generic", "Base")
auto1 = Auto("Chevrolet", "Captiva", 4)
moto1 = Moto("Honda", "XR300")

# Mostrar información
vehiculo1.mostrar_info()
vehiculo1.conducir()

print("\n")

auto1.mostrar_info()
print(f"Número de puertas: {auto1.puertas}")
auto1.conducir()

# Cambiar el número de puertas usando property
auto1.puertas = 2
print(f"Nuevo número de puertas: {auto1.puertas}")

print("\n")

moto1.mostrar_info()
moto1.conducir()
