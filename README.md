RSA-DLP

Este repositorio contiene la implementación y documentación de métodos relacionados con el cifrado RSA y problemas de Logaritmo Discreto (DLP, por sus siglas en inglés). El objetivo es proporcionar herramientas y ejemplos prácticos para comprender y analizar estos sistemas criptográficos.

Características

Implementación de RSA: Generación de claves, cifrado y descifrado de mensajes.

Ataques comunes a RSA: Factorización, pequeños exponentes y análisis de vulnerabilidades.

Problema del Logaritmo Discreto (DLP): Implementación de algoritmos para resolver logaritmos discretos en grupos finitos.

Aplicaciones prácticas: Ejemplos de uso real y simulaciones educativas.


Requisitos

Este proyecto utiliza Python 3.x y las siguientes dependencias:

sympy: Para operaciones matemáticas avanzadas.

numpy: Para cálculos y estructuras de datos.

matplotlib: Para visualización de datos (opcional).

Otras dependencias necesarias según el módulo.


Para instalarlas, puedes ejecutar:

pip install -r requirements.txt

Instalación

1. Clona el repositorio en tu máquina local:

git clone https://github.com/tuusuario/RSA-DLP.git
cd RSA-DLP


2. Instala las dependencias necesarias:

pip install -r requirements.txt


3. Ejecuta los scripts según los ejemplos proporcionados.



Uso

RSA

1. Generación de claves:

from rsa import generate_keys

public_key, private_key = generate_keys(bits=2048)


2. Cifrado y descifrado:

from rsa import encrypt, decrypt

ciphertext = encrypt("Mensaje secreto", public_key)
plaintext = decrypt(ciphertext, private_key)



DLP

1. Resolver logaritmos discretos:

from dlp import solve_dlp

result = solve_dlp(base=2, value=15, modulus=19)
print("Resultado:", result)


2. Visualizar algoritmos:

python dlp_visualization.py



Estructura del Proyecto

RSA-DLP/
├── rsa/                # Implementación de RSA
├── dlp/                # Algoritmos para resolver DLP
├── examples/           # Ejemplos y casos prácticos
├── tests/              # Pruebas unitarias
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo

Contribuciones

¡Contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras errores, no dudes en abrir un issue o enviar un pull request.

1. Haz un fork del proyecto.


2. Crea una rama para tu feature: git checkout -b feature/nueva-funcionalidad.


3. Haz commit de tus cambios: git commit -m "Añadida nueva funcionalidad".


4. Haz push a la rama: git push origin feature/nueva-funcionalidad.


5. Abre un pull request en este repositorio.



Licencia

Este proyecto está licenciado bajo la MIT License.


---

¿Te gustaría incluir alguna sección adicional, como más detalles técnicos o ejemplos?


