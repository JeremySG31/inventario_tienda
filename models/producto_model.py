from .db import conectar_bd

def insertar_producto(nombre, categoria, precio, stock):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
                       (nombre, categoria, precio, stock))
        conexion.commit()
        conexion.close()


def actualizar_producto(id_producto, nombre, categoria, precio, stock):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Productos 
            SET nombre = ?, categoria = ?, precio = ?, stock = ? 
            WHERE id = ?
        """, (nombre, categoria, precio, stock, id_producto))
        conexion.commit()
        conexion.close()


def obtener_productos():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos