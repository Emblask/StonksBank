from tkinter import Label, Entry, Button, messagebox
import datetime
import re

class Controlador:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.usuario_actual = None

    def crear_usuario(self, root, callback_volver):
        self.clear_frame(root)
        
        Label(root, text="Crear Usuario Nuevo", font=("Arial", 14), fg="#32CD32", bg="#000000").pack(pady=10)
        Label(root, text="Nombre de usuario:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_usuario = Entry(root, font=("Arial", 12))
        entry_usuario.pack(pady=5)

        Label(root, text="Contraseña:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_contrasena = Entry(root, show="*", font=("Arial", 12))
        entry_contrasena.pack(pady=5)

        Label(root, text="Nombre:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_nombre = Entry(root, font=("Arial", 12))
        entry_nombre.pack(pady=5)

        Label(root, text="Cédula:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_cedula = Entry(root, font=("Arial", 12))
        entry_cedula.pack(pady=5)

        Label(root, text="Fecha de Nacimiento (YYYY-MM-DD):", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_fecha_nacimiento = Entry(root, font=("Arial", 12))
        entry_fecha_nacimiento.pack(pady=5)

        Button(root, text="Registrar", command=lambda: self.registrar_usuario(
            entry_usuario.get(), entry_contrasena.get(), entry_nombre.get(),
            entry_cedula.get(), entry_fecha_nacimiento.get()
        ), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)

        Button(root, text="Volver al Menú", command=callback_volver, bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=5)

    def registrar_usuario(self, nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento):
        if not re.match(r"\d{4}-\d{2}-\d{2}", fecha_nacimiento):
            messagebox.showerror("Error", "Formato de fecha inválido. Usa YYYY-MM-DD.")
            return

        try:
            datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Usa el formato YYYY-MM-DD.")
            return

        self.repositorio.agregar_usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento)
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")

    def iniciar_sesion(self, root, callback_volver):
        self.clear_frame(root)

        Label(root, text="Iniciar Sesión", font=("Arial", 14), fg="#32CD32", bg="#000000").pack(pady=10)
        Label(root, text="Nombre de usuario:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_usuario = Entry(root, font=("Arial", 12))
        entry_usuario.pack(pady=5)

        Label(root, text="Contraseña:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_contrasena = Entry(root, show="*", font=("Arial", 12))
        entry_contrasena.pack(pady=5)

        Button(root, text="Iniciar Sesión", command=lambda: self.login_usuario(
            entry_usuario.get(), entry_contrasena.get(), root
        ), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)

        Button(root, text="Volver al Menú", command=callback_volver, bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=5)

    def login_usuario(self, nombre_usuario, contrasena, root):
        if self.repositorio.validar_usuario(nombre_usuario, contrasena):
            self.usuario_actual = nombre_usuario
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            self.mostrar_menu_principal(root)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar_menu_principal(self, root):
        self.clear_frame(root)

        Label(root, text=f"Bienvenido {self.usuario_actual}", font=("Arial", 14), fg="#32CD32", bg="#000000").pack(pady=10)

        Button(root, text="Realizar Transacciones", command=lambda: self.realizar_transacciones(root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)
        Button(root, text="Retirar Dinero", command=lambda: self.retirar_dinero(root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)
        Button(root, text="Consultar Saldo", command=self.consultar_saldo, bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)
        Button(root, text="Cerrar Sesión", command=lambda: self.cerrar_sesion(root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)

    def realizar_transacciones(self, root):
        self.clear_frame(root)
        
        Label(root, text="Transacción", font=("Arial", 14), fg="#32CD32", bg="#000000").pack(pady=10)
        Label(root, text="Valor a ingresar:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_valor = Entry(root, font=("Arial", 12))
        entry_valor.pack(pady=5)

        Button(root, text="Confirmar Transacción", command=lambda: self.confirmar_transaccion(entry_valor.get(), root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)
        Button(root, text="Volver", command=lambda: self.mostrar_menu_principal(root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=5)

    def confirmar_transaccion(self, valor, root):
        try:
            valor = float(valor)
            self.repositorio.usuarios[self.usuario_actual]["saldo"] += valor
            messagebox.showinfo("Éxito", f"Se han agregado {valor} a tu saldo.")
            self.mostrar_menu_principal(root)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico.")

    def retirar_dinero(self, root):
        self.clear_frame(root)
        
        Label(root, text="Retiro de Dinero", font=("Arial", 14), fg="#32CD32", bg="#000000").pack(pady=10)
        Label(root, text="Valor a retirar:", font=("Arial", 12), fg="white", bg="#000000").pack(pady=5)
        entry_valor = Entry(root, font=("Arial", 12))
        entry_valor.pack(pady=5)

        Button(root, text="Confirmar Retiro", command=lambda: self.confirmar_retiro(entry_valor.get(), root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=10)
        Button(root, text="Volver", command=lambda: self.mostrar_menu_principal(root), bg="#32CD32", fg="black", font=("Arial", 12)).pack(pady=5)

    def confirmar_retiro(self, valor, root):
        try:
            valor = float(valor)
            saldo_actual = self.repositorio.usuarios[self.usuario_actual]["saldo"]
            if valor > saldo_actual:
                messagebox.showerror("Error", "No tienes suficiente saldo para retirar esa cantidad.")
            else:
                self.repositorio.usuarios[self.usuario_actual]["saldo"] -= valor
                messagebox.showinfo("Éxito", f"Se han retirado {valor} de tu saldo.")
            self.mostrar_menu_principal(root)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico.")

    def consultar_saldo(self):
        if self.usuario_actual is None:
            messagebox.showerror("Error", "No has iniciado sesión.")
            return

        usuario_data = self.repositorio.usuarios.get(self.usuario_actual)
        if usuario_data is None or "saldo" not in usuario_data:
            messagebox.showerror("Error", "No se pudo obtener el saldo.")
            return

        saldo_actual = usuario_data["saldo"]
        messagebox.showinfo("Saldo Actual", f"Tu saldo actual es: {saldo_actual}.")

    def cerrar_sesion(self, root):
        self.usuario_actual = None
        messagebox.showinfo("Sesión Cerrada", "Has cerrado sesión exitosamente.")
        self.clear_frame(root)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
