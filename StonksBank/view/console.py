import sys
import os
from model.Bank import *


def main_menu():
    print("\n-- Menú Principal --")
    print("1. Crear usuario nuevo")
    print("2. Iniciar sesión")
    print ("3. Salir")
    opcion = input("Elige una opción: ")
    return opcion


def menu_sesion():
    print("\n-- Menú de Sesión --")
    print("1. Cambiar contraseña")
    opcion = input("Elige una opción: ")
    return opcion


def ejecutar():
    repositorio = RepositorioUsuario()
    controlador = ControladorUsuario(repositorio)

    while True:
        
        opcion = main_menu()

        os.system('cls' if os.name == 'nt' else 'clear')

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

            controlador.registrar_usuario(nombre_usuario, contrasena, nombre, cedula, fecha_nacimiento)

        elif opcion == "2":
            print("\n--- Iniciar Sesión ---")
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")

            if controlador.iniciar_sesion(nombre_usuario, contrasena):
                while True:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    opcion_sesion = menu_sesion()
                    if opcion_sesion == "1":
                        print("\n--- Cambiar Contraseña ---")
                        contrasena_actual = input("Contraseña actual: ")
                        nueva_contrasena = input("Nueva contraseña: ")
                        controlador.cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena)
                    elif opcion_sesion == "2":
                        print("\n--- Salir de Sesión ---")
                        break
                    else:
                        print("Opción inválida. Volviendo al menú principal.")
                        break
                    
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