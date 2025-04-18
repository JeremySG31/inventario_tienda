import tkinter as tk
from controllers.historial_controller import obtener_historial_ventas

def ventana_consultar_historial():
    ventana = tk.Toplevel()
    ventana.title("Historial de Ventas")

    frame = tk.Frame(ventana)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="ID Venta | Producto | Cantidad | Fecha", font=("Arial", 10, "bold")).pack()

    historial = obtener_historial_ventas()
    for venta in historial:
        texto = f"{venta[0]} | {venta[1]} | {venta[2]} | {venta[3]}"
        tk.Label(frame, text=texto).pack(anchor="w")
