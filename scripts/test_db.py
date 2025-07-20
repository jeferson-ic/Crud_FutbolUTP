# test_db.py
from db_utils import listar_jugadores

jugadores = listar_jugadores()
for j in jugadores:
    print(f"{j['nombre']} juega como {j['posicion']}")
