import hashlib

def hash_passwords(input_file, output_file):
    with open(input_file, 'r') as f:
        passwords = f.readlines()

    with open(output_file, 'w') as f:
        for password in passwords:
            password = password.strip()  # Eliminar cualquier espacio en blanco adicional
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            f.write(f"{password}: {hashed_password}\n")

if __name__ == "__main__":
    input_file = input("Por favor, introduce la ruta del archivo de contraseñas: ")
    output_file = "contraseñas_hashed.txt"
    hash_passwords(input_file, output_file)
    print("Contraseñas hasheadas y guardadas en contraseñas_hashed.txt")
