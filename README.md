# geoneo

# Script de Geolocalización

Este script de Python permite obtener información de geolocalización y almacenarla en una base de datos SQLite. Utiliza dos APIs diferentes para obtener datos de ubicación y geocodificación.

## Requisitos

- Python 3.x
- Paquetes requeridos: `requests`, `sqlite3`

## Instalación

1. Clona el repositorio o descarga los archivos del script.

```bash
git clone https://github.com/grisuno/geoneo.git
Instala los paquetes requeridos utilizando pip:
bash
Copy code
pip install requests
Uso
Obtén una clave de acceso para las APIs que se utilizan en el script:

IPStack para obtener información de ubicación.
PositionStack para realizar geocodificación.
Ejecuta el script con los siguientes argumentos:

bash
Copy code
python main.py <ip> <access_key>
Reemplaza <ip> con la dirección IP que deseas utilizar y <access_key> con tu clave de acceso correspondiente.

El script procesará la IP y realizará las consultas a las APIs. La información de ubicación se almacenará en una base de datos SQLite.

Puedes acceder a los datos almacenados ejecutando las siguientes funciones en el script:

print_table_structure(conn): Muestra la estructura de la tabla de ubicaciones en la base de datos.
print_table_data(conn): Muestra los datos almacenados en la tabla de ubicaciones.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error, tienes alguna idea de mejora o quieres agregar nuevas funcionalidades, siéntete libre de abrir un problema o enviar una solicitud de extracción.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.
