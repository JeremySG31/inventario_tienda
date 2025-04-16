from models import venta_model
from datetime import datetime

def registrar_venta(id_producto, cantidad):
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    venta_model.registrar_venta(id_producto, cantidad, fecha)

def ver_historial():
    return venta_model.obtener_historial_ventas()
