import sqlite3


def create_connection():
    connection = sqlite3.connect('gestok.db')
    return connection

# Crear tablas
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

