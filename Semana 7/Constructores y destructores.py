import os

class ArchivoTemporal:
    def __init__(self, nombre_archivo):
        # Constructor: se ejecuta cuando se crea el objeto
        self.nombre = nombre_archivo
        print(f" Constructor: Creando el archivo '{self.nombre}'...")

        # Crear el archivo y escribir contenido
        with open(self.nombre, 'w') as f:
            f.write("Este es un archivo temporal.\n")

    def mostrar_contenido(self):
        # Procedimiento adicional para mostrar el contenido del archivo
        print(f" Contenido de '{self.nombre}':")
        with open(self.nombre, 'r') as f:
            print(f.read())

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es destruido
        print(f" Destructor: Eliminando el archivo '{self.nombre}'...")
        if os.path.exists(self.nombre):
            os.remove(self.nombre)
            print(f"Archivo '{self.nombre}' eliminado correctamente.")
        else:
            print(f"El archivo '{self.nombre}' ya no existe.")

# Uso del objeto
if __name__ == "__main__":
    archivo = ArchivoTemporal("temporal.txt")  # Se llama al constructor
    archivo.mostrar_contenido()

    # Al finalizar el programa o eliminar el objeto, se llama al destructor automáticamente