import tkinter as tk
from controllers.producto_controller import registrar_nuevo_producto

def ventana_registrar_producto():
    ventana = tk.Toplevel()
    ventana.title("Registrar Producto")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Descripción:").grid(row=1, column=0)
    entry_descripcion = tk.Entry(ventana)
    entry_descripcion.grid(row=1, column=1)

    tk.Label(ventana, text="Precio:").grid(row=2, column=0)
    entry_precio = tk.Entry(ventana)
    entry_precio.grid(row=2, column=1)

    tk.Label(ventana, text="Stock:").grid(row=3, column=0)
    entry_stock = tk.Entry(ventana)
    entry_stock.grid(row=3, column=1)

    def guardar():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = float(entry_precio.get())
        stock = int(entry_stock.get())
        registrar_nuevo_producto(nombre, descripcion, precio, stock)
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)
