# db_utils.py
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="futbol_utp"
    )

def listar_jugadores():
    conn = conectar_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jugadores")
    jugadores = cursor.fetchall()
    conn.close()
    return jugadores
