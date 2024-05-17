import sqlite3
import os

# Defina o caminho absoluto para o arquivo do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'customermanager.db')

# Função para obter uma conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn