#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

print_red() {
    echo -e "${RED}$1${NC}"
}

print_red "Instalando colorama..."
pip install colorama

print_red "La biblioteca hashlib ya está incluida en la biblioteca estándar de Python."

print_red "Instalación completada."
