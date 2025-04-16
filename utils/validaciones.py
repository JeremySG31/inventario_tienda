def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
