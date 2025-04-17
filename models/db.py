# models/db.py
import sqlite3

def get_connection():
    return sqlite3.connect('inventario.db')

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER,
        cantidad INTEGER,
        fecha TEXT,
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    ''')

    conn.commit()
    conn.close()
