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
import uuid
import datetime

# Excepciones personalizadas
class UsuarioExistenteError(Exception):
    pass

class CedulaExistenteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

# Clase Usuario
class Usuario:
    def __init__(self, nombre_usuario: str, contrasena: str, nombre: str, cedula: str, fecha_nacimiento: datetime.date) -> None:
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena  # En un caso real, esta contraseña debería estar cifrada
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento

    def confirmar_contrasena(self, contrasena_actual: str) -> bool:
        return self.contrasena == contrasena_actual

    def actualizar_contrasena(self, contrasena_nueva: str) -> None:
        self.contrasena = contrasena_nueva

# Clase RepositorioUsuario
class RepositorioUsuario:
    def __init__(self):
        self.usuarios = {}

    def obtener_usuario(self, nombre_usuario: str) -> Usuario:
        return self.usuarios.get(nombre_usuario)

    def buscar_cedula(self, cedula: str) -> Usuario:
        for usuario in self.usuarios.values():
            if usuario.cedula == cedula:
                return usuario
        return None

    def agregar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.nombre_usuario] = usuario

    def actualizar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.nombre_usuario] = usuario

# Clase ControladorUsuario
class ControladorUsuario:
    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio
        self._usuario_actual = None

    def registrar_usuario(self, nombre_usuario: str, contrasena: str, nombre: str, cedula: str, fecha_nacimiento: datetime.date) -> bool:
        if self.repositorio.obtener_usuario(nombre_usuario):
            raise UsuarioExistenteError(f"El nombre de usuario '{nombre_usuario}' ya está registrado.")
        if self.repositorio.buscar_cedula(cedula):
            raise CedulaExistenteError(f"La cédula '{cedula}' ya está registrada.")
        nuevo_usuario = Usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento)
        self.repositorio.agregar_usuario(nuevo_usuario)
        print("Usuario registrado con éxito.")
        return True

    def iniciar_sesion(self, nombre_usuario: str, contrasena: str) -> bool:
        usuario = self.repositorio.obtener_usuario(nombre_usuario)
        if usuario and usuario.confirmar_contrasena(contrasena):
            self._usuario_actual = usuario
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}.")
            return True
        else:
            raise ValueError("Nombre de usuario o contraseña incorrectos.")  # Usamos una excepción estándar para errores de autenticación

    def usuario_actual(self) -> Usuario:
        return self._usuario_actual 

    def cambiar_contrasena(self, nombre_usuario: str, contrasena_actual: str, nueva_contrasena: str) -> bool:
        usuario = self.repositorio.obtener_usuario(nombre_usuario)
        if usuario and usuario.confirmar_contrasena(contrasena_actual):
            usuario.actualizar_contrasena(nueva_contrasena)
            self.repositorio.actualizar_usuario(usuario)
            print("Contraseña actualizada con éxito.")
            return True
        else:
            print("Contraseña actual incorrecta.")
            return False

# Clase Cuenta
class Cuenta:
    def __init__(self, tipo_cuenta: str, saldo: float = 0.0):
        self.id_cuenta = str(uuid.uuid4())  # Genera un ID único para la cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.historial_transacciones = []

    def deducir_monto(self, monto: float) -> bool:
        if self.saldo >= monto:
            self.saldo -= monto
            self.historial_transacciones.append(["Deducción", monto])
            return True
        return False

    def agregar_monto(self, monto: float) -> None:
        self.saldo += monto
        self.historial_transacciones.append(["Depósito", monto])

# Clase RepositorioCuenta
class RepositorioCuenta:
    def __init__(self):
        self.cuentas = {}

    def obtener_cuenta(self, id_cuenta: str) -> Cuenta:
        return self.cuentas.get(id_cuenta)

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        self.cuentas[cuenta.id_cuenta] = cuenta

# Clase ControladorCuenta
class ControladorCuenta:
    def __init__(self, repositorio: RepositorioCuenta):
        self.repositorio = repositorio

    def crear_cuenta(self, usuario: Usuario, tipo_cuenta: str) -> Cuenta:
        nueva_cuenta = Cuenta(tipo_cuenta)
        self.repositorio.agregar_cuenta(nueva_cuenta)
        print(f"Cuenta de tipo '{tipo_cuenta}' creada con éxito. ID: {nueva_cuenta.id_cuenta}")
        return nueva_cuenta

    def realizar_transferencia(self, cuenta_origen: Cuenta, cuenta_destino: Cuenta, monto: float) -> bool:
        if cuenta_origen.deducir_monto(monto):
            cuenta_destino.agregar_monto(monto)
            print(f"Transferencia de {monto} realizada con éxito.")
            return True
        else:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar la transferencia.")

    def retirar_dinero(self, cuenta: Cuenta, monto: float) -> bool:
        if cuenta.deducir_monto(monto):
            print(f"Retiro de {monto} realizado con éxito.")
            return True
        else:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar el retiro.")
