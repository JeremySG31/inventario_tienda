import tkinter as tk
from views.registrar_producto import ventana_registrar
from views.consultar_inventario import ventana_consultar
from views.registrar_venta import ventana_venta

def main_view():
    ventana = tk.Tk()
    ventana.title("Sistema de Inventario")

    tk.Button(ventana, text="Registrar Producto", command=ventana_registrar).pack()
    tk.Button(ventana, text="Consultar Inventario", command=ventana_consultar).pack()
    tk.Button(ventana, text="Registrar Venta", command=ventana_venta).pack()

    ventana.mainloop()