import tkinter as tk
from controllers.producto_controller import editar_producto, obtener_producto

def ventana_actualizar():
    ventana = tk.Toplevel()
    ventana.title("Actualizar Producto")

    tk.Label(ventana, text="ID Producto").grid(row=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    def cargar():
        id_prod = int(id_entry.get())
        producto = obtener_producto(id_prod)
        if producto:
            nombre_var.set(producto[1])
            categoria_var.set(producto[2])
            precio_var.set(producto[3])
            stock_var.set(producto[4])

    nombre_var = tk.StringVar()
    categoria_var = tk.StringVar()
    precio_var = tk.StringVar()
    stock_var = tk.StringVar()

    tk.Label(ventana, text="Nombre").grid(row=1)
    tk.Label(ventana, text="Categoría").grid(row=2)
    tk.Label(ventana, text="Precio").grid(row=3)
    tk.Label(ventana, text="Stock").grid(row=4)

    nombre = tk.Entry(ventana, textvariable=nombre_var)
    categoria = tk.Entry(ventana, textvariable=categoria_var)
    precio = tk.Entry(ventana, textvariable=precio_var)
    stock = tk.Entry(ventana, textvariable=stock_var)

    nombre.grid(row=1, column=1)
    categoria.grid(row=2, column=1)
    precio.grid(row=3, column=1)
    stock.grid(row=4, column=1)

    def guardar():
        editar_producto(int(id_entry.get()), nombre.get(), categoria.get(), float(precio.get()), int(stock.get()))
        ventana.destroy()

    tk.Button(ventana, text="Cargar", command=cargar).grid(row=0, column=2)
    tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2)