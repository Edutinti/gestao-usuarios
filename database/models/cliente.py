import sqlite3
from database.database import get_db_connection

class Cliente():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @staticmethod
    def conectarDb():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL)")
        conn.commit()
    
        return conn, cursor
