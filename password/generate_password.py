import random
import string
from colorama import init, Fore, Style

init(autoreset=True)

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError(Fore.RED + "Al menos una opción de caracteres debe estar habilitada")

    return ''.join(random.choice(chars) for _ in range(length))

def save_passwords(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

def main():
    try:
        print(Fore.CYAN + "Generador de Contraseñas Aleatorias")
        print(Style.RESET_ALL)

        num_passwords = int(input("Número de contraseñas a generar: "))
        length = int(input("Longitud de la contraseña: "))
        uppercase = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
        lowercase = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
        digits = input("¿Incluir dígitos? (s/n): ").lower() == 's'
        special_chars = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

        passwords = [generate_password(length, uppercase, lowercase, digits, special_chars) for _ in range(num_passwords)]
        print("\n" + Fore.GREEN + "Contraseñas generadas:")
        for password in passwords:
            print(password)

        save_option = input("\n¿Desea guardar las contraseñas en un archivo? (s/n): ").lower()
        if save_option == 's':
            filename = input("Nombre del archivo para guardar las contraseñas: ")
            save_passwords(passwords, filename)
            print(Fore.YELLOW + f"\nLas contraseñas se han guardado en '{filename}'")
    except ValueError as ve:
        print(Fore.RED + "Error:", ve)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nOperación cancelada por el usuario.")

if __name__ == "__main__":
    main()
