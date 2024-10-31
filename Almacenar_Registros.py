import requests
from tkinter import messagebox

class GestorAPI:
    def __init__(self):
        self.url = "https://671be4212c842d92c381a521.mockapi.io/Productos"
        self.records = []

    def cargar_todos(self):
        """Carga todos los registros de la API."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.records = response.json()
            return self.records
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error al obtener los registros: {e}")
            return None

    def cargar_por_id(self, product_id):
        """Busca un registro específico por ID."""
        return next((rec for rec in self.records if rec['id'] == product_id), None)
