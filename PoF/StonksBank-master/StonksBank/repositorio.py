import json
import os

class RepositorioUsuario:
    def __init__(self, archivo_usuarios='usuarios.json'):
        self.archivo_usuarios = archivo_usuarios
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, 'r') as archivo:
                return json.load(archivo)
        return {}

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as archivo:
            json.dump(self.usuarios, archivo, indent=4)

    def agregar_usuario(self, nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento, saldo=0):
        self.usuarios[nombre_usuario] = {
            'contrasena': contrasena,
            'nombre': nombre,
            'cedula': cedula,
            'fecha_nacimiento': fecha_nacimiento,
            'saldo': saldo
        }
        self.guardar_usuarios()

    def validar_usuario(self, nombre_usuario, contrasena):
        usuario = self.usuarios.get(nombre_usuario)
        return usuario and usuario['contrasena'] == contrasena

    def cambiar_contrasena(self, nombre_usuario, nueva_contrasena):
        if nombre_usuario in self.usuarios:
            self.usuarios[nombre_usuario]['contrasena'] = nueva_contrasena
            self.guardar_usuarios()

    def restar_saldo(self, nombre_usuario, monto):
        if nombre_usuario in self.usuarios:
            saldo = self.usuarios[nombre_usuario].get("saldo", 0)
            if saldo >= monto:
                self.usuarios[nombre_usuario]["saldo"] = saldo - monto
                self.guardar_usuarios()
                return True
        return False

    def aumentar_saldo(self, nombre_usuario, monto):
        if nombre_usuario in self.usuarios:
            saldo = self.usuarios[nombre_usuario].get("saldo", 0)
            self.usuarios[nombre_usuario]["saldo"] = saldo + monto
            self.guardar_usuarios()
