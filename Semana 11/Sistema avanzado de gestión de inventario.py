# -*- coding: utf-8 -*-
"""
Sistema Avanzado de Gestión de Inventarios
------------------------------------------
- Uso de Programación Orientada a Objetos (POO).
- Uso de colecciones (diccionario) para gestión eficiente.
- Persistencia con archivos (guardar/cargar inventario).
- Manejo de excepciones en operaciones de archivo.
"""

import json   # Usamos JSON para serializar y deserializar colecciones


class Producto:
    """Representa un producto con ID, nombre, cantidad y precio."""

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID:{self.id} | Nombre:{self.nombre} | Cantidad:{self.cantidad} | Precio:${self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto en diccionario para guardarlo en JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Reconstruye un producto a partir de un diccionario (cargar JSON)."""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    """Clase Inventario que maneja productos usando un diccionario."""

    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario: clave = ID del producto
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {p["id"]: Producto.from_dict(p) for p in data}
                print("Inventario cargado correctamente desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, se creará uno nuevo al guardar.")
            self.productos = {}
        except json.JSONDecodeError:
            print("Archivo corrupto. Se iniciará un inventario vacío.")
            self.productos = {}
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar inventario: {e}")

    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                data = [p.to_dict() for p in self.productos.values()]
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar inventario: {e}")

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()
            print("Producto actualizado.")
        else:
            print("No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        """Devuelve productos cuyo nombre contenga la palabra buscada."""
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n=== INVENTARIO COMPLETO ===")
            for p in self.productos.values():
                print(p)


# =====================
# Interfaz de consola
# =====================
def menu():
    inv = Inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.añadir_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad_txt = input("Nueva cantidad (enter para omitir): ")
            precio_txt = input("Nuevo precio (enter para omitir): ")
            cantidad = int(cantidad_txt) if cantidad_txt else None
            precio = float(precio_txt) if precio_txt else None
            inv.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inv.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()