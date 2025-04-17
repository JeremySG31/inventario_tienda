# controllers/historial_controller.py
from models.db import get_connection

def obtener_historial_ventas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT v.id, p.nombre, v.cantidad, v.fecha
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
    ''')
    historial = cursor.fetchall()
    conn.close()
    return historial
