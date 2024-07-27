# Generador y Hasheador de Contraseñas

Este proyecto consta de dos scripts en Python:

1. **Generador de Contraseñas Aleatorias:** Genera contraseñas aleatorias basadas en las opciones especificadas por el usuario.
2. **Hasheador de Contraseñas:** Lee contraseñas desde un archivo, las hashea utilizando SHA-256 y guarda los resultados en un archivo de salida.

## Requisitos

- Python 3.x
- [Colorama](https://pypi.org/project/colorama/) (para el generador de contraseñas, para la gestión de colores en la terminal)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/generate.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd password
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip install colorama
    ```

## Scripts

### Generador de Contraseñas Aleatorias

Este script genera contraseñas aleatorias según los parámetros especificados por el usuario y ofrece la opción de guardarlas en un archivo.

#### Uso

1. **Ejecuta el script:**

    ```bash
    python generate_password.py
    ```

2. **Introduce los parámetros solicitados:**
    - Número de contraseñas a generar.
    - Longitud de cada contraseña.
    - Opciones para incluir letras mayúsculas, minúsculas, dígitos y caracteres especiales.

3. **Decide si deseas guardar las contraseñas en un archivo y proporciona el nombre del archivo si es necesario.**

#### Descripción de Opciones

- **Número de contraseñas a generar:** Define cuántas contraseñas quieres crear.
- **Longitud de la contraseña:** Especifica la longitud de cada contraseña generada.
- **Incluir letras mayúsculas/minúsculas:** Elige si deseas incluir letras mayúsculas o minúsculas en las contraseñas.
- **Incluir dígitos y caracteres especiales:** Decide si deseas que las contraseñas incluyan dígitos y/o caracteres especiales.

#### Manejo de Errores

- **ValueError:** Se muestra si ninguna opción de caracteres está habilitada.
- **KeyboardInterrupt:** El script maneja la interrupción del teclado (Ctrl+C) para cerrar el programa de manera segura.

### Hasheador de Contraseñas

Este script lee contraseñas desde un archivo, las hashea utilizando SHA-256 y guarda los resultados en un archivo de salida.

#### Uso

1. **Ejecuta el script:**

    ```bash
    python hash_passwords.py
    ```

2. **Introduce la ruta del archivo de contraseñas cuando se te solicite.** El archivo de salida será `contraseñas_hashed.txt`.

#### Descripción de Opciones

- **Archivo de contraseñas:** Archivo de entrada que contiene contraseñas en texto plano, una por línea.
- **Archivo de salida:** Archivo que contendrá cada contraseña en texto plano seguida de su hash SHA-256.

#### Manejo de Errores

- **FileNotFoundError:** Se muestra si el archivo de contraseñas no se encuentra en la ruta especificada.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Utiliza estos scripts para generar y hashear contraseñas de manera segura y eficiente.
