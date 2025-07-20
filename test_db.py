# test_db.py
from db import get_connection

conn = get_connection()
print("Conexión exitosa" if conn else "Error en la conexión")
conn.close()
