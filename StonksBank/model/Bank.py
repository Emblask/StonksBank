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
        self.contrasena = contrasena  
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
            raise ValueError("Nombre de usuario o contraseña incorrectos.")

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
        self.bloqueada = False

    def deducir_monto(self, monto: float) -> bool:
        if self.saldo >= monto and not self.bloqueada:
            self.saldo -= monto
            self.historial_transacciones.append(["Deducción", monto])
            return True
        return False

    def agregar_monto(self, monto: float) -> None:
        if not self.bloqueada:
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

    def mostrar_saldo_e_historial(self, cuenta: Cuenta) -> None:
        print(f"Saldo actual: {cuenta.saldo}")
        print("Historial de transacciones:")
        for transaccion in cuenta.historial_transacciones:
            print(f"{transaccion[0]} de {transaccion[1]}")

# Clase ControladorReporte
class ControladorReporte:
    def __init__(self, cuenta: Cuenta):
        self.cuenta = cuenta

    def generar_reporte(self) -> dict:
        return {
            "id_cuenta": self.cuenta.id_cuenta,
            "tipo_cuenta": self.cuenta.tipo_cuenta,
            "saldo": self.cuenta.saldo,
            "historial_transacciones": self.cuenta.historial_transacciones,
        }

    def mostrar_reporte_en_pantalla(self) -> None:
        datos = self.generar_reporte()
        print(f"Reporte de la cuenta ID: {datos['id_cuenta']}")
        print(f"Tipo de cuenta: {datos['tipo_cuenta']}")
        print(f"Saldo: {datos['saldo']}")
        print("Historial de transacciones:")
        for transaccion in datos["historial_transacciones"]:
            print(f"  - {transaccion[0]} de {transaccion[1]}")

    def descargar_reporte(self) -> None:
        print("Descargando reporte...")

# Clase ControladorAdmin
class ControladorAdmin:
    def __init__(self, cuenta_repo: RepositorioCuenta):
        self.cuenta_repo = cuenta_repo

    def bloquear_cuenta(self, cuenta: Cuenta) -> None:
        cuenta.bloqueada = True
        print(f"Cuenta ID: {cuenta.id_cuenta} ha sido bloqueada.")

    def desbloquear_cuenta(self, cuenta: Cuenta) -> None:
        cuenta.bloqueada = False
        print(f"Cuenta ID: {cuenta.id_cuenta} ha sido desbloqueada.")
