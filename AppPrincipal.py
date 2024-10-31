import tkinter as tk
from Almacenar_Registros import GestorAPI
from Productos import TablaProductos
from Id import EntradaID

class AppPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Crear instancias de las clases
        gestor_api = GestorAPI ()
        tabla = TablaProductos(root)
        EntradaID (root, gestor_api, tabla)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppPrincipal(root)
    root.mainloop()
