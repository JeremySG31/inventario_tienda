from models import venta_model
from datetime import datetime

def registrar_nueva_venta(producto_id, cantidad):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    venta_model.registrar_venta(producto_id, cantidad, fecha_actual)
