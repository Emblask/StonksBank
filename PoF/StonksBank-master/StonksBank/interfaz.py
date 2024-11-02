import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class InterfazBanco:
    def __init__(self, root, controlador):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("660x480")
        self.root.configure(bg="#FFFFFF")
        self.controlador = controlador

        # Frame para el logo
        self.frame_logo = tk.Frame(self.root, bg="#000000", width=300)
        self.frame_logo.pack(side="left", fill="y")

        self.logo_img = Image.open("StonksBank-master/StonksBank/imagenes/logo.png")
        self.logo_img = self.logo_img.resize((300, 300), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo_img)
        self.label_logo = tk.Label(self.frame_logo, image=self.logo, bg="#000000")
        self.label_logo.pack(pady=70)

        self.frame_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.frame_menu.pack(pady=(70, 0))

        self.label_title = tk.Label(self.frame_menu, text="Bienvenido a Stonks Bank", font=("Arial", 18, "bold"), fg="#030918", bg="#FFFFFF")
        self.label_title.pack(pady=50)

        self.btn_crear_usuario = tk.Button(self.frame_menu, text="Crear Usuario Nuevo", command=self.crear_usuario, bg="#008000", fg="#FFFFFF", font=("Arial", 12), width=25)
        self.btn_crear_usuario.pack(pady=10)

        self.btn_iniciar_sesion = tk.Button(self.frame_menu, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#008000", fg="#FFFFFF", font=("Arial", 12), width=25)
        self.btn_iniciar_sesion.pack(pady=10)

        self.btn_salir = tk.Button(self.frame_menu, text="Salir", command=self.root.quit, bg="#008000", fg="#FFFFFF", font=("Arial", 12), width=25)
        self.btn_salir.pack(pady=10)

    def crear_usuario(self):
        self.controlador.crear_usuario(self.root, self.mostrar_menu)

    def iniciar_sesion(self):
        self.controlador.iniciar_sesion(self.root, self.mostrar_menu)

    def mostrar_menu(self):
        self.root.destroy()
        nuevo_root = tk.Tk()
        nueva_interfaz = InterfazBanco(nuevo_root, self.controlador)
        nuevo_root.mainloop()
