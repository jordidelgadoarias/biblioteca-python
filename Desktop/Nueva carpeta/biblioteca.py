import json

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def agregar(self):
        print(f"Libro agregado: {self.titulo} por {self.autor} (ISBN: {self.isbn})")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro {self.titulo} prestado con éxito.")
        else:
            print(f"El libro {self.titulo} ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro {self.titulo} devuelto con éxito.")
        else:
            print(f"El libro {self.titulo} ya estaba disponible.")

    def mostrar(self):
        estado = "Sí" if self.disponible else "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")

    def buscar(self, isbn):
        if self.isbn == isbn:
            self.mostrar()
            return True
        return False

def cargar_libros():
    try:
        with open("biblioteca.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Libros de ejemplo si el archivo no existe
        libros_ejemplo = [
            {
                "titulo": "La ciudad de los prodigios",
                "autor": "Eduardo Mendoza",
                "isbn": "9788432231513",
                "disponible": True
            },
            {
                "titulo": "La sombra del viento",
                "autor": "Carlos Ruiz Zafón",
                "isbn": "9788408163350",
                "disponible": True
            }
        ]
        guardar_libros(libros_ejemplo)
        return libros_ejemplo

def guardar_libros(libros):
    with open("biblioteca.json", "w") as archivo:
        json.dump(libros, archivo, indent=4)

def menu():
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    return input("Elige una opción: ")

def main():
    biblioteca = cargar_libros()

    while True:
        opcion = menu()

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            nuevo_libro = {
                "titulo": titulo,
                "autor": autor,
                "isbn": isbn,
                "disponible": True
            }
            biblioteca.append(nuevo_libro)
            guardar_libros(biblioteca)
            print("Libro agregado con éxito.")

        elif opcion == '2':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro["isbn"] == isbn:
                    if libro["disponible"]:
                        libro["disponible"] = False
                        guardar_libros(biblioteca)
                        print(f"Libro {libro['titulo']} prestado con éxito.")
                    else:
                        print(f"El libro {libro['titulo']} ya está prestado.")
                    break
            else:
                print("Libro no encontrado.")

        elif opcion == '3':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro["isbn"] == isbn:
                    if not libro["disponible"]:
                        libro["disponible"] = True
                        guardar_libros(biblioteca)
                        print(f"Libro {libro['titulo']} devuelto con éxito.")
                    else:
                        print(f"El libro {libro['titulo']} ya estaba disponible.")
                    break
            else:
                print("Libro no encontrado.")

        elif opcion == '4':
            if not biblioteca:
                print("No hay libros en la biblioteca.")
            else:
                for libro in biblioteca:
                    estado = "Sí" if libro["disponible"] else "No"
                    print(f"- {libro['titulo']} ({libro['autor']}) - ISBN: {libro['isbn']} - Disponible: {estado}")

        elif opcion == '5':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro["isbn"] == isbn:
                    estado = "Sí" if libro["disponible"] else "No"
                    print(f"- {libro['titulo']} ({libro['autor']}) - ISBN: {libro['isbn']} - Disponible: {estado}")
                    break
            else:
                print("Libro no encontrado.")

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
    