import sqlite3


class Cliente():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @staticmethod
    def conectarDb():
        conn = sqlite3.connect('customermanager.db')
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL)")
        conn.commit()

        return conn, cursor

    def inserirCliente(self):
        conn = sqlite3.connect('customermanager.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)", (self.nome, self.email))
        conn.commit()
        conn.close()

    def verCliente(cliente_id):
        conn = sqlite3.connect('customermanager.db')
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
        consulta = cursor.fetchone()
        conn.close()

        return consulta

    

