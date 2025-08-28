class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    # Cargar productos desde el archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    id_producto, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, se creará uno nuevo.")
            open(self.archivo, "w", encoding="utf-8").close()
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    # Guardar productos en archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    # Agregar producto
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El ID ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print("Producto agregado correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            p = self.productos[id_producto]
            if nombre: p.nombre = nombre
            if cantidad is not None: p.cantidad = cantidad
            if precio is not None: p.precio = precio
            self.guardar_inventario()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Mostrar productos
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(f"ID: {p.id} | {p.nombre} | Cant: {p.cantidad} | Precio: ${p.precio:.2f}")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    inventario = Inventario()

    # Agregar productos
    inventario.agregar_producto(Producto("001", "Laptop", 5, 750.00))
    inventario.agregar_producto(Producto("002", "Mouse", 20, 15.50))

    # Mostrar
    inventario.mostrar_productos()

    # Actualizar
    inventario.actualizar_producto("001", cantidad=10, precio=700.00)

    # Eliminar
    inventario.eliminar_producto("002")

    # Mostrar otra vez
    inventario.mostrar_productos()