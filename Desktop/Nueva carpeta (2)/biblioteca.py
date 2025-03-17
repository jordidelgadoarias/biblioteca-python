import json
import random  # Importamos el módulo random para seleccionar frases al azar

# Lista de frases célebres para mostrar en caso de error
frases_celebres = [
    "La libertad no vale la pena, si no conlleva la libertad de errar. -Mahatma Gandhi",
    "El único hombre que no se equivoca es el que nunca hace nada. -Goethe",
    "Errar es humano, perdonar es divino. -Alexander Pope",
    "El fracaso es simplemente la oportunidad de comenzar de nuevo, esta vez de forma más inteligente. -Henry Ford",
    "No tengas miedo de cometer errores, pero asegúrate de no cometer el mismo error dos veces. -Akio Morita",
    "El éxito es la capacidad de ir de fracaso en fracaso sin perder el entusiasmo. -Winston Churchill",
    "Un error no se convierte en un fracaso hasta que te niegas a corregirlo. -John F. Kennedy",
    "La experiencia es simplemente el nombre que le damos a nuestros errores. -Oscar Wilde",
    "El hombre que nunca ha cometido un error nunca ha intentado nada nuevo. -Albert Einstein",
    "Aprende de los errores de los demás. No vivirás lo suficiente para cometerlos todos tú mismo. -Eleanor Roosevelt"
]

# Función para validar el ISBN
def validar_isbn(isbn):
    # Verifica que el ISBN tenga exactamente 13 caracteres y que todos sean dígitos numéricos
    return len(isbn) == 13 and isbn.isdigit()

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

def agregar_libro(biblioteca):
    while True:
        # Pedir al usuario que ingrese el título, autor e ISBN del libro
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        
        # Validar el ISBN usando la función validar_isbn
        if not validar_isbn(isbn):
            # Si el ISBN no es válido, mostrar un mensaje de error y una frase célebre al azar
            print("\nEl ISBN introducido es erróneo. ¿Probar de nuevo?")
            frase_aleatoria = random.choice(frases_celebres)  # Seleccionar una frase al azar
            print(frase_aleatoria)  # Mostrar la frase célebre
            respuesta = input("¿Intentar de nuevo? (sí/no): ").strip().lower()
            
            if respuesta == 'no' or respuesta == 'n':
                # Si el usuario elige "no", volver al menú principal
                print("Volviendo al menú principal...")
                return
            else:
                # Si el usuario elige "sí", continuar con el bucle para intentar de nuevo
                continue
        
        # Verificar si el ISBN ya existe en la biblioteca
        for libro in biblioteca:
            if libro["isbn"] == isbn:
                # Si el ISBN ya existe, mostrar un mensaje de error y volver al menú principal
                print("El libro con este ISBN ya existe en la biblioteca.")
                return
        
        # Si el ISBN es válido y no está duplicado, crear un nuevo libro
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn,
            "disponible": True
        }
        # Agregar el nuevo libro a la lista de la biblioteca
        biblioteca.append(nuevo_libro)
        # Guardar la lista actualizada en el archivo JSON
        guardar_libros(biblioteca)
        # Mostrar un mensaje de éxito
        print("Libro agregado con éxito.")
        return  # Salir de la función después de agregar el libro

def main():
    biblioteca = cargar_libros()

    while True:
        opcion = menu()

        if opcion == '1':
            agregar_libro(biblioteca)

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