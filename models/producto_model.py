from models.db import get_connection

def insertar_producto(nombre, descripcion, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, precio, stock)
        VALUES (?, ?, ?, ?)
    ''', (nombre, descripcion, precio, stock))
    conn.commit()
    conn.close()
