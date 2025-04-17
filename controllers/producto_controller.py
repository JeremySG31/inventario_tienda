# controllers/producto_controller.py
from models import producto_model

def registrar_nuevo_producto(nombre, descripcion, precio, stock):
    producto_model.insertar_producto(nombre, descripcion, precio, stock)
