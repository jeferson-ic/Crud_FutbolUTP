# ejemplos.py
"""
Este archivo contiene ejemplos y documentación en Python
que podrían usarse en el futuro como parte del sistema.
"""

# Ejemplo 1: Consumir API de jugadores
"""
import requests

url = "http://localhost:5000/api/jugadores"
response = requests.get(url)

if response.status_code == 200:
    jugadores = response.json()
    for jugador in jugadores:
        print(jugador['nombre'], jugador['posición'])
"""

# Ejemplo 2: Conexión a MySQL
"""
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="futbol_utp"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM jugadores")
for row in cursor.fetchall():
    print(row)

conn.close()
"""


