from .db import conectar_bd

def registrar_venta(id_producto, cantidad, fecha):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Ventas (id_producto, cantidad, fecha)
            VALUES (?, ?, ?)
        """, (id_producto, cantidad, fecha))
        conexion.commit()
        conexion.close()


def obtener_historial_ventas():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Ventas")
        ventas = cursor.fetchall()
        conexion.close()
        return ventas