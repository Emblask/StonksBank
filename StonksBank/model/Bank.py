"""

Registrar al nuevo usuario en el sistema. registrar_usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento) ControladorUsuario
comprobar si usuario o nombre_usuario ya existen obtener_usuario(nombre_usuario):Usuario buscar_cedula(cedula):Usuario RepositorioUsuario
Crear una nueva instancia de la clase Usuario. __init__(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento) Usuario
Agregar el usuario al repositorio de usuarios. agregar_usuario(usuario) RepositorioUsuario

Iniciar el proceso de inicio de sesión para el usuario. iniciar_sesion(nombre_usuario, contrasena) ControladorUsuario
Buscar y validar el usuario en el repositorio de usuarios. obtener_usuario(nombre_usuario) RepositorioUsuario
Confirmar contraseña confirmar_contraseña(contrasena_actual): Bool Usuario
Mantener conexión usuario_actual:Usuario ControladorUsuario

Iniciar el proceso para cambiar la contraseña del usuario. cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) ControladorUsuario
Buscar y validar el usuario en el repositorio de usuarios. obtener_usuario(nombre_usuario) RepositorioUsuario
Confirmar contraseña actual confirmar_contraseña(contrasena_actual): Bool Usuario
Actualizar la contraseña en el objeto Usuario. actualizar_contrasena(contrasena_nueva):str Usuario
Guardar el usuario actualizado en el repositorio. actualizar_usuario(usuario)RepositorioUsuario
"""

import datetime




class Usuario:
    def __init__(self, nombre_usuario:str, contrasena:str, nombre:str, cedula:str, fecha_nacimiento:datetime) -> None:
        # Inicializar atributos del usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena  # En un caso real, esta contraseña debería estar cifrada
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento

    def confirmar_contrasena(self, contrasena_actual:str) -> bool:
        # Verificar si la contraseña ingresada coincide
        return self.contrasena == contrasena_actual
    
    
    def actualizar_contrasena(self, contrasena_nueva:str) -> str:
        # Actualizar la contraseña del usuario
        self.contrasena = contrasena_nueva


class RepositorioUsuario:
    def __init__(self):
        self.usuarios = {}  # Diccionario para almacenar usuarios con nombre_usuario como clave


    def obtener_usuario(self, nombre_usuario:str) -> Usuario:
        # Retornar el usuario si existe en el repositorio
        return self.usuarios.get(nombre_usuario)
    

    def buscar_cedula(self, cedula:str) -> Usuario:
        # Buscar usuario por cédula
        for usuario in self.usuarios.values():
            if usuario.cedula == cedula:
                return usuario
        return None
    

    def agregar_usuario(self, usuario:Usuario) -> None:
        # Agregar el usuario al repositorio
        self.usuarios[usuario.nombre_usuario] = usuario


    def actualizar_usuario(self, usuario:Usuario) -> None:
        # Actualizar el usuario en el repositorio
        self.usuarios[usuario.nombre_usuario] = usuario
        
class ControladorUsuario:
    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio
        self._usuario_actual = None


    def registrar_usuario(self, nombre_usuario:str, contrasena:str, nombre:str, cedula:str, fecha_nacimiento:datetime) -> None:
        # Verificar si el nombre de usuario o la cédula ya existen
        if self.repositorio.obtener_usuario(nombre_usuario):
            print(f"El nombre de usuario '{nombre_usuario}' ya está registrado.")
            return False
        if self.repositorio.buscar_cedula(cedula):
            print(f"La cédula '{cedula}' ya está registrada.")
            return False
        # Crear una nueva instancia de Usuario
        nuevo_usuario = Usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento)
        
        # Agregar el usuario al repositorio
        self.repositorio.agregar_usuario(nuevo_usuario)
        print("Usuario registrado con éxito.")
        return True
    

    def iniciar_sesion(self, nombre_usuario:str, contrasena:str) -> bool:
        # Buscar el usuario en el repositorio
        usuario = self.repositorio.obtener_usuario(nombre_usuario)
        
        # Validar usuario y contraseña
        if usuario and usuario.confirmar_contrasena(contrasena):
            self._usuario_actual = usuario
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}.")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False
        

    def usuario_actual(self) -> Usuario:
        # Retornar el usuario actual en sesión
        return self._usuario_actual 
    

    def cambiar_contrasena(self, nombre_usuario:str, contrasena_actual:str, nueva_contrasena:str) -> bool:
        # Buscar y validar el usuario en el repositorio
        usuario = self.repositorio.obtener_usuario(nombre_usuario)
        
        if usuario and usuario.confirmar_contrasena(contrasena_actual):
            # Actualizar la contraseña
            usuario.actualizar_contrasena(nueva_contrasena)
            
            # Guardar el usuario actualizado en el repositorio
            self.repositorio.actualizar_usuario(usuario)
            print("Contraseña actualizada con éxito.")
            return True
        else:
            print("Contraseña actual incorrecta.")
            return False
