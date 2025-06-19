# tienda_snacks.py

# Clase que representa un snack
class Snack:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.codigo} | {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            total = self.precio * cantidad
            print(f"Venta realizada: {cantidad} x {self.nombre} = ${total:.2f}")
            return total
        else:
            print(f"No hay suficiente stock de {self.nombre}. Solo quedan {self.stock} unidades.")
            return 0

# Clase que representa la tienda de snacks
class TiendaDeSnack:
    def __init__(self, nombre):
        self.nombre = nombre
        self.snacks = []

    def agregar_snack(self, snack):
        self.snacks.append(snack)

    def mostrar_inventario(self):
        print(f"\nInventario de la tienda {self.nombre}:")
        for snack in self.snacks:
            snack.mostrar_info()

    def vender_snack(self, codigo, cantidad):
        for snack in self.snacks:
            if snack.codigo == codigo:
                return snack.vender(cantidad)
        print("Snack no encontrado.")
        return 0

# --- Simulación de la tienda de snacks ---
def main():
    tienda = TiendaDeSnack("Snack Ecuador")

    # Crear snacks
    snack1 = Snack("A1", "Papas fritas picantes", 1.80, 10)
    snack2 = Snack("B2", "Chocolate sabor menta", 2.50, 5)
    snack3 = Snack("C3", "Galleta Oreo", 2.00, 9)

    # Agregar al inventario
    tienda.agregar_snack(snack1)
    tienda.agregar_snack(snack2)
    tienda.agregar_snack(snack3)

    # Mostrar inventario inicial
    tienda.mostrar_inventario()

    # Realizar ventas
    tienda.vender_snack("B2", 2)
    tienda.vender_snack("C3", 10)  # Intento de venta con stock insuficiente

    # Mostrar inventario después de las ventas
    tienda.mostrar_inventario()

if __name__ == "__main__":
    main()
