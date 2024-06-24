# Generador y Hasheador de Contraseñas

Este proyecto contiene scripts en Python para generar contraseñas aleatorias y para hashear contraseñas almacenadas en un archivo.

## Scripts

### 1. generate_password.py

Este script genera contraseñas aleatorias según las preferencias del usuario y las muestra por pantalla. También permite guardar las contraseñas en un archivo.

#### Uso

1. Clona o descarga este repositorio en tu máquina local.
2. Abre una terminal y navega al directorio donde se encuentra el script `generate_password.py`.
3. Ejecuta el script con Python:

   ```bash
   python generate_password.py
Sigue las instrucciones en pantalla para especificar el número de contraseñas a generar, longitud, y qué tipos de caracteres incluir.

Opcionalmente, puedes guardar las contraseñas generadas en un archivo.

2.hash_passwords.py
Este script toma un archivo de contraseñas en texto plano y genera hashes SHA-256 para cada contraseña. Los hashes junto con las contraseñas originales se guardan en un archivo de salida.

Uso
Asegúrate de tener un archivo de contraseñas en texto plano preparado.

Abre una terminal y navega al directorio donde se encuentra el script hash_passwords.py.

Ejecuta el script con Python:
python hash_passwords.py

Introduce la ruta del archivo de contraseñas cuando se te solicite.

Las contraseñas hasheadas se guardarán en el archivo contraseñas_hashed.txt en el mismo directorio.

3. install_librerias.sh
Este script de shell simplifica la instalación de las dependencias necesarias para ejecutar generate_password.py, específicamente la biblioteca colorama.

Uso
Abre una terminal y navega al directorio donde se encuentra el script install_librerias.sh.

Ejecuta el script:
bash install_librerias.sh

Sigue las instrucciones en pantalla para completar la instalación de colorama.

Requisitos
Python 3.x
Biblioteca colorama


