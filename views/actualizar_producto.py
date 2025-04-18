import tkinter as tk
from models.db import get_connection

def ventana_actualizar_producto():
    ventana = tk.Toplevel()
    ventana.title("Actualizar Producto")

    tk.Label(ventana, text="ID del Producto:").grid(row=0, column=0)
    entry_id = tk.Entry(ventana)
    entry_id.grid(row=0, column=1)

    tk.Label(ventana, text="Nuevo Stock:").grid(row=1, column=0)
    entry_stock = tk.Entry(ventana)
    entry_stock.grid(row=1, column=1)

    def actualizar():
        producto_id = int(entry_id.get())
        nuevo_stock = int(entry_stock.get())

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE productos SET stock = ? WHERE id = ?', (nuevo_stock, producto_id))
        conn.commit()
        conn.close()
        ventana.destroy()

    tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=2, column=0, columnspan=2, pady=10)
