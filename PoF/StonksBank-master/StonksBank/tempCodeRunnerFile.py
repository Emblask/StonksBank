if __name__ == "__main__":
    root = Tk()

    repositorio = RepositorioUsuario()  # Crear el repositorio de usuarios
    controlador = Controlador(repositorio)  # Pasar el repositorio al controlador

    app = InterfazBanco(root, controlador)  # Pasar el controlador a la interfaz
    root.mainloop()  # Ejecutar la aplicación
