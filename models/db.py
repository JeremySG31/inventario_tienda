import pyodbc

def conectar_bd():
    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=InventarioTienda;'
            'UID=tu_usuario;'
            'PWD=tu_contraseña'
        )
        return conexion
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        return None