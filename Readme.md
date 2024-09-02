# StonksBank

## Descripción

**StonksBank** es una aplicación de gestión bancaria diseñada para ayudar a un banco a manejar la información de sus usuarios, cuentas, transacciones y más. Los usuarios del banco pueden registrarse, iniciar sesión, crear cuentas bancarias, realizar transacciones entre cuentas, ver el saldo y el historial de transacciones, entre otras funcionalidades. Además, el personal administrativo del banco puede generar reportes y gestionar las cuentas de los usuarios.

## Estructura del Proyecto

La estructura del proyecto sigue una organización estándar de aplicaciones en Python, con carpetas específicas para modelos, servicios, controladores, archivos estáticos, plantillas, y pruebas. A continuación se detalla la función de cada carpeta y archivo:

### Carpetas

- **`StonksBank/`**: Carpeta principal del proyecto, que contiene todos los módulos y archivos de la aplicación.

  - **`models/`**: Contiene las definiciones de las clases que representan los modelos de datos del sistema, como. Estas clases definen la estructura de los datos y las relaciones entre ellos.

  - **`services/`**: Contiene la lógica de negocio de la aplicación, como la gestión de usuarios, cuentas, y transacciones. Aquí se implementan los métodos para realizar operaciones como transferencias de dinero, cambios de contraseña, y generación de reportes.

  - **`resources/`**:  contiene archivos y recursos necesarios para el funcionamiento de la aplicación, excluyendo el código fuente. como Imagenes, videos, sonidos, etc.

- **`tests/`**: Contiene los archivos de prueba (test) que verifican la funcionalidad de la aplicación. Aquí se incluyen pruebas unitarias y pruebas de integración para asegurarse de que todos los componentes funcionen correctamente.

### Archivos

- **`StonksBank/__init__.py`**: Archivo que convierte la carpeta `StonksBank` en un módulo de Python. Permite importar submódulos desde esta carpeta.

- **`StonksBank/app.py`**: Archivo principal de la aplicación. Contiene el código para iniciar la aplicación, definir las rutas y configurar la interacción entre los controladores y la lógica de negocio.

- **`StonksBank/config.py`**: Archivo de configuración de la aplicación. Contiene parámetros de configuración como la base de datos, claves secretas, y otras variables de entorno.

- **`README.md`**: Este archivo. Proporciona una descripción general del proyecto, su estructura y su propósito.

- **`.gitignore`**: Archivo que especifica qué archivos o carpetas deben ser ignorados por Git. Suele incluir archivos de configuración local, bases de datos temporales, y otros archivos que no deberían ser versionados.

- **`requirements.txt`**: Archivo que contiene una lista de dependencias de Python que se deben instalar para que la aplicación funcione correctamente. Se utiliza para instalar las dependencias con pip.

- **`setup.py`**: Archivo que define la configuración para distribuir e instalar el paquete Python. Incluye información sobre el nombre del paquete, versión, autor, y dependencias.

- **`LICENSE.txt`**: contiene la licencia bajo la cual se distribuye este proyecto. La licencia define los términos y condiciones para el uso, modificación y redistribución del código y otros recursos del proyecto. Es importante leer y comprender la licencia para asegurar el cumplimiento de los derechos y responsabilidades legales.

## Cómo Iniciar el Proyecto

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Emblask39/Stonks_Bank.git
2. **Navegar al directorio del proyecto**:
    ```bash
    cd StonksBank
3. **Crear un entorno virtual (opcional pero recomendado)**:
    ```bash
    python3 -m venv venvsource venv/bin/activate  
    # En Windows: venv\Scripts\activate
4. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
5. **Ejecutar la aplicación**:
    ```bash
    python StonksBank/app.py


