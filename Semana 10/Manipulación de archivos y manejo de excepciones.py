import json
import os

# -----------------------------
# Clase Producto
# -----------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

# -----------------------------
# Clase Inventario
# -----------------------------
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    # Cargar inventario desde archivo
    def cargar_inventario(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.productos = [Producto(**p) for p in data]
            else:
                # Si no existe, se crea vacío
                with open(self.archivo, "w", encoding="utf-8") as f:
                    json.dump([], f)
                self.productos = []
        except (FileNotFoundError, PermissionError) as e:
            print(f"[ERROR] No se pudo leer el archivo: {e}")
            self.productos = []
        except json.JSONDecodeError:
            print("[ERROR] El archivo está corrupto. Se reiniciará vacío.")
            self.productos = []
            self.guardar_inventario()

    # Guardar inventario en archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
            return True
        except PermissionError:
            print("[ERROR] No tienes permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"[ERROR] Ocurrió un problema al guardar: {e}")
            return False

    # Añadir producto
    def anadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print(f"[ERROR] Ya existe un producto con ID {producto.id}")
            return
        self.productos.append(producto)
        if self.guardar_inventario():
            print(f"[OK] Producto {producto.nombre} añadido exitosamente.")

    # Actualizar producto
    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id:
                if nombre: p.nombre = nombre
                if cantidad is not None: p.cantidad = cantidad
                if precio is not None: p.precio = precio
                if self.guardar_inventario():
                    print(f"[OK] Producto con ID {id} actualizado.")
                return
        print(f"[ERROR] No se encontró producto con ID {id}.")

    # Eliminar producto
    def eliminar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                if self.guardar_inventario():
                    print(f"[OK] Producto con ID {id} eliminado.")
                return
        print(f"[ERROR] No se encontró producto con ID {id}.")

    # Buscar producto
    def buscar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                return p
        return None

    # Listar productos
    def listar_productos(self):
        if not self.productos:
            print("[INFO] El inventario está vacío.")
        else:
            for p in self.productos:
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

# -----------------------------
# Interfaz de Usuario en Consola
# -----------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Listar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.anadir_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == "2":
            id = input("Ingrese ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacío si no cambia): ")
            cantidad = input("Nueva cantidad (vacío si no cambia): ")
            precio = input("Nuevo precio (vacío si no cambia): ")
            inventario.actualizar_producto(
                id,
                nombre if nombre else None,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "3":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "4":
            id = input("Ingrese ID del producto a buscar: ")
            p = inventario.buscar_producto(id)
            if p:
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
            else:
                print("[ERROR] Producto no encontrado.")

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("[ERROR] Opción no válida.")

# -----------------------------
# Ejecución principal
# -----------------------------
if __name__ == "__main__":
    menu()