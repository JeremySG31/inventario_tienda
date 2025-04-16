import tkinter as tk
from controllers.producto_controller import listar_productos

def ventana_consultar():
    ventana = tk.Toplevel()
    ventana.title("Inventario")
    productos = listar_productos()

    for i, producto in enumerate(productos):
        tk.Label(ventana, text=str(producto)).grid(row=i)