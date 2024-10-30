import sys
import os
import datetime
import uuid  # Para la generación de ID únicos de cuenta
from model.Bank import *  # Verifica que todas las clases estén en el módulo Bank

# Menús de opciones
def main_menu():
    print("\n-- Menú Principal --")
    print("1. Crear usuario nuevo")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def menu_sesion():
    print("\n-- Menú de Sesión --")
    print("1. Cambiar contraseña")
    print("2. Crear cuenta bancaria")
    print("3. Realizar transferencia")
    print("4. Retirar dinero")
    print("5. Salir de sesión")
    opcion = input("Elige una opción: ")
    return opcion

# Ejecución del sistema
def ejecutar():
    # Inicialización de repositorios y controladores
    repositorio_usuarios = RepositorioUsuario()
    repositorio_cuentas = RepositorioCuenta()
    controlador_usuarios = ControladorUsuario(repositorio_usuarios)
    controlador_cuentas = ControladorCuenta(repositorio_cuentas)

    while True:
        opcion = main_menu()
        #os.system('cls' if os.name == 'nt' else 'clear')

        if opcion == "1":
            print("\n--- Crear Usuario Nuevo ---")
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

            try:
                fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            except ValueError:
                print("Formato de fecha incorrecto. Usa el formato YYYY-MM-DD.")
                continue

            controlador_usuarios.registrar_usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento)

        elif opcion == "2":
            print("\n--- Iniciar Sesión ---")
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")

            if controlador_usuarios.iniciar_sesion(nombre_usuario, contrasena):
                usuario_actual = controlador_usuarios.usuario_actual()

                while True:
                    #os.system('cls' if os.name == 'nt' else 'clear')
                    opcion_sesion = menu_sesion()

                    if opcion_sesion == "1":
                        print("\n--- Cambiar Contraseña ---")
                        contrasena_actual = input("Contraseña actual: ")
                        nueva_contrasena = input("Nueva contraseña: ")
                        confirmar_contrasena = input("Confirmar nueva contraseña: ")

                        if nueva_contrasena != confirmar_contrasena:
                            print("Las contraseñas no coinciden.")
                        else:
                            if controlador_usuarios.cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena):
                                print("Contraseña cambiada correctamente.")

                    elif opcion_sesion == "2":
                        print("\n--- Crear Cuenta Bancaria ---")
                        tipo_cuenta = input("Tipo de cuenta (e.g., Ahorros, Corriente): ")
                        # Crear la cuenta con ID único
                        cuenta = controlador_cuentas.crear_cuenta(usuario_actual, tipo_cuenta)
                        print(f"Cuenta de tipo '{tipo_cuenta}' creada con éxito.")

                    elif opcion_sesion == "3":
                        print("\n--- Realizar Transferencia ---")
                        id_cuenta_origen = input("ID de cuenta origen: ")
                        id_cuenta_destino = input("ID de cuenta destino: ")
                        try:
                            monto = float(input("Monto a transferir: "))
                        except ValueError:
                            print("Monto inválido. Asegúrate de ingresar un número.")
                            continue

                        cuenta_origen = repositorio_cuentas.obtener_cuenta(id_cuenta_origen)
                        cuenta_destino = repositorio_cuentas.obtener_cuenta(id_cuenta_destino)

                        if cuenta_origen and cuenta_destino:
                            if controlador_cuentas.realizar_transferencia(cuenta_origen, cuenta_destino, monto):
                                print("Transferencia realizada con éxito.")
                        else:
                            print("Una o ambas cuentas no existen.")

                    elif opcion_sesion == "4":
                        print("\n--- Retirar Dinero ---")
                        id_cuenta = input("ID de la cuenta: ")
                        try:
                            monto = float(input("Monto a retirar: "))
                        except ValueError:
                            print("Monto inválido. Asegúrate de ingresar un número.")
                            continue
                        
                        cuenta = repositorio_cuentas.obtener_cuenta(id_cuenta)
                        if cuenta:
                            if controlador_cuentas.retirar_dinero(cuenta, monto):
                                print("Retiro realizado con éxito.")
                            else:
                                print("Saldo insuficiente.")
                        else:
                            print("La cuenta no existe.")

                    elif opcion_sesion == "5":
                        print("\n--- Saliendo de Sesión ---")
                        break

                    else:
                        print("Opción inválida. Inténtalo de nuevo.")

            else:
                print("No se pudo iniciar sesión. Volviendo al menú principal.")
            
        elif opcion == "3":
            print("\n--- Saliendo del Sistema ---")
            sys.exit(0)

        else:
            print("Opción inválida. Inténtalo de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    ejecutar()
