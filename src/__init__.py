import tkinter as tk
from tkinter import ttk

class PaginaInicio:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa de Métodos Numéricos")

        self.root.geometry("900x600")

        bienvenida_label = ttk.Label(root, text="Bienvenido al Programa de Métodos Numéricos", font=("Arial", 16))
        bienvenida_label.pack(pady=20)

        
        boton_iniciar = ttk.Button(root, text="Iniciar Programa", command=self.abrir_programa)
        boton_iniciar.pack(pady=10)

    def abrir_programa(self):
       
        print("Abriendo el programa principal")

root = tk.Tk()
app = PaginaInicio(root)

root.mainloop()
