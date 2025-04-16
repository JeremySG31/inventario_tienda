import tkinter as tk
from controllers.producto_controller import agregar_producto

def ventana_registrar():
    ventana = tk.Toplevel()
    ventana.title("Registrar Producto")

    tk.Label(ventana, text="Nombre").grid(row=0)
    tk.Label(ventana, text="Categoría").grid(row=1)
    tk.Label(ventana, text="Precio").grid(row=2)
    tk.Label(ventana, text="Stock").grid(row=3)

    nombre = tk.Entry(ventana)
    categoria = tk.Entry(ventana)
    precio = tk.Entry(ventana)
    stock = tk.Entry(ventana)

    nombre.grid(row=0, column=1)
    categoria.grid(row=1, column=1)
    precio.grid(row=2, column=1)
    stock.grid(row=3, column=1)

    def guardar():
        agregar_producto(nombre.get(), categoria.get(), float(precio.get()), int(stock.get()))
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2)