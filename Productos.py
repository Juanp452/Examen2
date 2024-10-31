import tkinter as tk
from tkinter import ttk

class TablaProductos:
    def __init__(self, root):
        # Treeview para mostrar detalles de productos
        self.tree = ttk.Treeview(root, columns=("ID", "Productos", "Colores", "Código", "Precio"), show='headings')
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Configurar encabezados de la tabla
        self.tree.heading("ID", text="ID")
        self.tree.heading("Productos", text="Productos")
        self.tree.heading("Colores", text="Colores de los productos")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Precio", text="Precio")

        # Añadir un scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def limpiar_tabla(self):
        """Limpia todos los datos en la tabla."""
        for row in self.tree.get_children():
            self.tree.delete(row)

    def agregar_registro(self, record):
        """Agrega un registro a la tabla."""
        self.tree.insert("", tk.END, values=(record['id'], record['Productos'], record['coloresdelosproductos'], record['Codigo'], record['Precio']))

    def agregar_registros(self, records):
        """Agrega múltiples registros a la tabla."""
        self.limpiar_tabla()
        for record in records:
            self.agregar_registro(record)
