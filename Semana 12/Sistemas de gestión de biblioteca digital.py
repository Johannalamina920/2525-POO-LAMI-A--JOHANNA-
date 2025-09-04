# ==========================
# Sistema de Gestión de Biblioteca Digital
# ==========================

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tupla para título y autor (inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario {ID: Usuario}
        self.ids_usuarios = set()  # Conjunto para evitar duplicados

    # -------------------------
    # Gestión de libros
    # -------------------------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print(f"No existe un libro con ISBN {isbn} en la biblioteca.")

    # -------------------------
    # Gestión de usuarios
    # -------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print(f"No existe un usuario con ID {id_usuario}.")

    # -------------------------
    # Gestión de préstamos
    # -------------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # Lo sacamos de los disponibles
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # Regresamos el libro al catálogo
                print(f"Libro devuelto: {libro} por {usuario.nombre}")
                return
        print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")

    # -------------------------
    # Búsquedas
    # -------------------------
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # -------------------------
    # Listar libros prestados
    # -------------------------
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f" - {libro}")
        else:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")


# ==========================
# PRUEBA DEL SISTEMA
# ==========================

if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Orgullo y prejuicio", "Jane Austen", "Clásico", "111")
    libro2 = Libro("Historia de Roma", "Tito Livio", "Historia", "222")
    libro3 = Libro("Leyendas Latinoamericanas", "Nancy Crespo", "Cuentos infantiles", "333")

    # Agregar libros
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Carolina", "U001")
    usuario2 = Usuario("Leonardo", "U002")

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "111")
    biblioteca.prestar_libro("U002", "222")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("U001")

    # Devolver libro
    biblioteca.devolver_libro("U001", "111")

    # Buscar libros
    print("\n Búsqueda por categoría 'Clásico':")
    resultados = biblioteca.buscar_libro("categoria", "Programación")
    for r in resultados:
        print(f" - {r}")