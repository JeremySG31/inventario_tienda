import tkinter as tk
from controllers.venta_controller import registrar_venta

def ventana_venta():
    ventana = tk.Toplevel()
    ventana.title("Registrar Venta")

    tk.Label(ventana, text="ID Producto").grid(row=0)
    tk.Label(ventana, text="Cantidad").grid(row=1)

    id_producto = tk.Entry(ventana)
    cantidad = tk.Entry(ventana)

    id_producto.grid(row=0, column=1)
    cantidad.grid(row=1, column=1)

    def guardar():
        registrar_venta(int(id_producto.get()), int(cantidad.get()))
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=2, column=0, columnspan=2)