import tkinter as tk
from tkinter import messagebox, ttk
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("800x600")
        self.root.resizable(False, False)  # Ventana no dimensionable

        # Frame para cargar registros
        self.frame_load = tk.Frame(root)
        self.frame_load.pack(pady=10)

        # Entrada para ID de producto
        self.entry_id = tk.Entry(self.frame_load)
        self.entry_id.pack(side=tk.LEFT, padx=5)

        # Botón para cargar por ID
        self.btn_load_by_id = tk.Button(self.frame_load, text="Cargar por ID", command=self.load_record_by_id)
        self.btn_load_by_id.pack(side=tk.LEFT)

        # Botón para cargar todos los registros
        self.btn_load_all = tk.Button(root, text="Cargar Todos los Registros", command=self.load_all_records)
        self.btn_load_all.pack(pady=10)

        # Botón para actualizar la lista
        self.btn_update_list = tk.Button(root, text="Actualizar Lista", command=self.load_all_records)
        self.btn_update_list.pack(pady=10)

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

    def load_all_records(self):
        """Carga todos los registros de la base de datos."""
        try:
            response = requests.get("https://671be4212c842d92c381a521.mockapi.io/Productos")
            response.raise_for_status()
            self.records = response.json()  # Guarda todos los registros

            # Limpiar la tabla anterior
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Agregar cada producto a la tabla
            for record in self.records:
                self.tree.insert("", tk.END, values=(record['id'], record['Productos'], record['coloresdelosproductos'], record['Codigo'], record['Precio']))

            messagebox.showinfo("Carga Completa", "Todos los registros han sido cargados.")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error al obtener los registros: {e}")

    def load_record_by_id(self):
        """Carga un registro específico basado en el ID ingresado."""
        product_id = self.entry_id.get().strip()  # Obtener el ID del campo de entrada
        if not product_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID.")
            return

        # Buscar el registro por ID
        if hasattr(self, 'records'):
            record = next((rec for rec in self.records if rec['id'] == product_id), None)
            if record:
                # Limpiar la tabla anterior
                for row in self.tree.get_children():
                    self.tree.delete(row)
                # Agregar el registro a la tabla
                self.tree.insert("", tk.END, values=(record['id'], record['Productos'], record['coloresdelosproductos'], record['Codigo'], record['Precio']))
            else:
                messagebox.showwarning("No Encontrado", f"No se encontró un producto con ID: {product_id}")
        else:
            messagebox.showwarning("Carga de Registros", "Por favor, cargue primero todos los registros.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
