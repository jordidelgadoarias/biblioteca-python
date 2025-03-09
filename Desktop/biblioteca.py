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
    biblioteca = []

    while True:
        opcion = menu()

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            biblioteca.append(nuevo_libro)
            nuevo_libro.agregar()

        elif opcion == '2':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro.buscar(isbn):
                    libro.prestar()
                    break
            else:
                print("Libro no encontrado.")

        elif opcion == '3':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro.buscar(isbn):
                    libro.devolver()
                    break
            else:
                print("Libro no encontrado.")

        elif opcion == '4':
            if not biblioteca:
                print("No hay libros en la biblioteca.")
            else:
                for libro in biblioteca:
                    libro.mostrar()

        elif opcion == '5':
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro.buscar(isbn):
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