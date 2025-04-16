from models import producto_model

def agregar_producto(nombre, categoria, precio, stock):
    producto_model.insertar_producto(nombre, categoria, precio, stock)

def editar_producto(id_producto, nombre, categoria, precio, stock):
    producto_model.actualizar_producto(id_producto, nombre, categoria, precio, stock)

def listar_productos():
    return producto_model.obtener_productos()