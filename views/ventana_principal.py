import tkinter as tk
from views.registrar_producto import ventana_registrar_producto
from views.consultar_inventario import ventana_consultar_inventario
from views.registrar_venta import ventana_registrar_venta
from views.actualizar_producto import ventana_actualizar_producto
from views.consultar_historial import ventana_consultar_historial  

def ventana_principal(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Sistema de Gestión de Inventario", font=("Arial", 16)).pack(pady=10)

    tk.Button(frame, text="Registrar Producto", width=25, command=ventana_registrar_producto).pack(pady=5)
    tk.Button(frame, text="Consultar Inventario", width=25, command=ventana_consultar_inventario).pack(pady=5)
    tk.Button(frame, text="Registrar Venta", width=25, command=ventana_registrar_venta).pack(pady=5)
    tk.Button(frame, text="Actualizar Producto", width=25, command=ventana_actualizar_producto).pack(pady=5)
    tk.Button(frame, text="Consultar Historial de Ventas", width=25, command=ventana_consultar_historial).pack(pady=5)  
