# views/consultar_inventario.py
import tkinter as tk
from models.db import get_connection

def ventana_consultar_inventario():
    ventana = tk.Toplevel()
    ventana.title("Inventario de Productos")

    frame = tk.Frame(ventana)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="ID | Nombre | Descripción | Precio | Stock", font=("Arial", 10, "bold")).pack()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()

    for producto in productos:
        texto = f"{producto[0]} | {producto[1]} | {producto[2]} | S/.{producto[3]} | {producto[4]}"
        tk.Label(frame, text=texto).pack(anchor="w")
