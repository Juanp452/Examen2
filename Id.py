import tkinter as tk
from tkinter import messagebox

class EntradaID:
    def __init__(self, root, gestor_api, tabla):
        self.gestor_api = gestor_api
        self.tabla = tabla

        # Frame para cargar registros
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Entrada para ID de producto
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.pack(side=tk.LEFT, padx=5)

        # Botón para cargar por ID
        self.btn_load_by_id = tk.Button(self.frame, text="Cargar por ID", command=self.cargar_por_id)
        self.btn_load_by_id.pack(side=tk.LEFT)

        # Botón para cargar todos los registros
        self.btn_load_all = tk.Button(root, text="Cargar Todos los Registros", command=self.cargar_todos)
        self.btn_load_all.pack(pady=10)

    def cargar_todos(self):
        """Carga todos los registros de la API y los muestra en la tabla."""
        records = self.gestor_api.cargar_todos()
        if records:
            self.tabla.agregar_registros(records)
            messagebox.showinfo("Carga Completa", "Todos los registros han sido cargados.")

    def cargar_por_id(self):
        """Carga un registro específico basado en el ID ingresado."""
        product_id = self.entry_id.get().strip()
        if not product_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID.")
            return

        if not self.gestor_api.records:
            messagebox.showwarning("Carga de Registros", "Por favor, cargue primero todos los registros.")
            return

        record = self.gestor_api.cargar_por_id(product_id)
        if record:
            self.tabla.limpiar_tabla()
            self.tabla.agregar_registro(record)
        else:
            messagebox.showwarning("No Encontrado", f"No se encontró un producto con ID: {product_id}")
