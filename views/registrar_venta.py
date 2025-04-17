# views/registrar_venta.py
import tkinter as tk
from controllers.venta_controller import registrar_nueva_venta
from models.db import get_connection

def ventana_registrar_venta():
    ventana = tk.Toplevel()
    ventana.title("Registrar Venta")

    tk.Label(ventana, text="ID Producto:").grid(row=0, column=0)
    entry_producto_id = tk.Entry(ventana)
    entry_producto_id.grid(row=0, column=1)

    tk.Label(ventana, text="Cantidad:").grid(row=1, column=0)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.grid(row=1, column=1)

    def guardar_venta():
        producto_id = int(entry_producto_id.get())
        cantidad = int(entry_cantidad.get())
        registrar_nueva_venta(producto_id, cantidad)
        ventana.destroy()

    tk.Button(ventana, text="Guardar Venta", command=guardar_venta).grid(row=2, column=0, columnspan=2, pady=10)

    # Opcional: Mostrar productos para facilitar
    tk.Label(ventana, text="Lista de Productos:", font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM productos")
    productos = cursor.fetchall()
    conn.close()

    fila = 4
    for prod in productos:
        texto = f"{prod[0]} - {prod[1]}"
        tk.Label(ventana, text=texto).grid(row=fila, column=0, columnspan=2)
        fila += 1
