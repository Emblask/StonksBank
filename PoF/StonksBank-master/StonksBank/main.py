from tkinter import Tk
from interfaz import InterfazBanco
from controlador import Controlador
from repositorio import RepositorioUsuario

def main():
    # Crear la ventana principal de la aplicación
    root = Tk()

    # Inicializar el repositorio de usuarios
    repositorio = RepositorioUsuario()

    # Inicializar el controlador con el repositorio
    controlador = Controlador(repositorio)

    # Inicializar la interfaz gráfica y pasar el controlador
    app = InterfazBanco(root, controlador)

    # Ejecutar la aplicación
    root.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
