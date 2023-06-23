import http.client
import urllib.parse
import sqlite3
import os
import requests
import json
import sys


def insert_location(conn, data):
    # Obtener los datos del JSON
    location_data = data['data'][0]
    location_values = (
        data['latitude'], data['longitude'], data['type'], str(location_data['name']),
        location_data['number'], location_data['postal_code'], location_data['street'],
        location_data['region'], data['region_code'], location_data['county'], location_data['locality'],
        location_data['administrative_area'], location_data['neighbourhood'], location_data['country'],
        location_data['country_code'], location_data['continent'], location_data['label']
    )

    # Insertar datos en la tabla
    cursor = conn.cursor()
    cursor.execute("INSERT INTO location (latitude, longitude, type, name, number, postal_code, street, region, region_code, county, locality, administrative_area, neighbourhood, country, country_code, continent, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   location_values)


def print_table_structure(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(location)")
    table_structure = cursor.fetchall()

    # Imprimir la estructura de la tabla
    print("Estructura de la tabla:")
    for column in table_structure:
        print(column)


def print_table_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM location")
    table_data = cursor.fetchall()

    # Imprimir los datos de la tabla
    print("Datos de la tabla:")
    for row in table_data:
        print(row)


def create_database(database_file):
    # Crear la base de datos si no existe
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS location (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        latitude REAL,
                        longitude REAL,
                        type TEXT,
                        name TEXT,
                        number TEXT,
                        postal_code TEXT,
                        street TEXT,
                        region TEXT,
                        region_code TEXT,
                        county TEXT,
                        locality TEXT,
                        administrative_area TEXT,
                        neighbourhood TEXT,
                        country TEXT,
                        country_code TEXT,
                        continent TEXT,
                        label TEXT
                    )''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()


def get_location_data(ip, access_key):
    response = requests.get(f'http://api.ipstack.com/{ip}?access_key={access_key}')

    if response.status_code == 200:
        return response.json()
    else:
        print("Error al realizar la solicitud a la API.")
        return None


def get_geocoding_data(query, region):
    params = {
        'access_key': 'xxxxxxxxxxxxxxxxxxxxxxxx',
        'query': query,
        'region': region,
        'limit': 1,
    }
    encoded_params = urllib.parse.urlencode(params)
    conn = http.client.HTTPConnection('api.positionstack.com')
    conn.request('GET', '/v1/forward?{}'.format(encoded_params))

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode('utf-8'))


def print_banner():
    banner = """
  ####   ######   ####   #    #  ######   ####
 #    #  #       #    #  ##   #  #       #    #
 #       #####   #    #  # #  #  #####   #    #
 #  ###  #       #    #  #  # #  #       #    #
 #    #  #       #    #  #   ##  #       #    #
  ####   ######   ####   #    #  ######   ####
   """
    print(banner)


if __name__ == '__main__':
    print_banner()

    if len(sys.argv) != 3:
        print("Uso: python main.py <ip> <access_key>")
        sys.exit(1)

    ip = sys.argv[1]
    access_key = sys.argv[2]

    database_file = 'database.db'

    if os.path.exists(database_file):
        print("La base de datos ya existe.")
        # Aquí puedes agregar el código adicional que desees ejecutar si la base de datos ya existe
    else:
        create_database(database_file)
        print("La base de datos ha sido creada.")

    location_data = get_location_data(ip, access_key)

    if location_data:
        query = f"{location_data['city']}, latitude: {location_data['latitude']}, longitude: {location_data['longitude']}"
        geocoding_data = get_geocoding_data(query, location_data['region_name'])

        if geocoding_data:
            merged_data = {**geocoding_data, **location_data}
            insert_location(sqlite3.connect(database_file), merged_data)
            print("La ubicación se ha insertado en la base de datos.")

            # Mostrar la estructura de la tabla y los datos
            with sqlite3.connect(database_file) as conn:
                print_table_structure(conn)
                print_table_data(conn)
        else:
            print("No se pudo obtener información de geocodificación.")
