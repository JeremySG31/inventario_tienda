# models/venta_model.py
from models.db import get_connection

def registrar_venta(producto_id, cantidad, fecha):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ventas (producto_id, cantidad, fecha)
        VALUES (?, ?, ?)
    ''', (producto_id, cantidad, fecha))
    conn.commit()
    conn.close()
