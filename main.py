# main.py
import tkinter as tk
from models.db import create_tables
from views.ventana_principal import ventana_principal

def main():
    create_tables()
    root = tk.Tk()
    root.title("Sistema de Gestión de Inventario")
    ventana_principal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
