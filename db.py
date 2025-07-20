import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # tu usuario de MySQL
        password="root",           # tu contraseña (si tienes)
        database="futbol_utp"  # nombre de tu base de datos
    )
