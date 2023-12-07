import tkinter as tk
from tkinter import ttk
import sv_ttk
from metodosNumericos.secante import dataInput
from tkinter import BooleanVar

class SecanteContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
   
        sv_ttk.use_light_theme()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.criterio = BooleanVar()
        # Widgets Frame
        self.inputFrame = ttk.LabelFrame(self, text='Ingrese los datos')
        self.inputFrame.grid(row=0, column=0, padx=20, pady=10)

        self.function_entry = ttk.Entry(self.inputFrame)
        self.function_label = ttk.Label(self.inputFrame, text='f(x)')
        self.function_label.grid(row=0,column=0, padx=5, pady=(0, 5), sticky="ew")
        self.function_entry.grid(row=0,column=1, padx=5, pady=5, sticky="ew")

        self.x_anterior_entry = ttk.Entry(self.inputFrame)
        self.x_anterior_label = ttk.Label(self.inputFrame, text='xi-1')
        self.x_anterior_label.grid(row=1,column=0,padx=5, pady=(0, 5), sticky="ew")
        self.x_anterior_entry.grid(row=1,column=1, padx=5, pady=5, sticky="ew")

        self.x_actual_entry = ttk.Entry(self.inputFrame)
        self.x_actual_label = ttk.Label(self.inputFrame, text="xi")
        self.x_actual_label.grid(row=2,column=0,padx=5, pady=(0, 5), sticky="ew")
        self.x_actual_entry.grid(row=2,column=1, padx=5, pady=5, sticky="ew")

        self.tolerancia_entry = ttk.Entry(self.inputFrame)
        self.tolerancia_label = ttk.Label(self.inputFrame, text='Criterio')
        self.tolerancia_label.grid(row=3,column=0,padx=5, pady=(0, 5), sticky="ew")
        self.tolerancia_entry.grid(row=3,column=1, padx=5, pady=5, sticky="ew")

        self.calcular_button = ttk.Button(self.inputFrame, text='Calcular', command=self.showResult)
        self.calcular_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew") 

        self.iteracionesButton = ttk.Radiobutton(self.inputFrame, text="Iteraciones", value=True, variable=self.criterio)
        self.iteracionesButton.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        self.ErrorButton = ttk.Radiobutton(self.inputFrame, text="Error", value=False, variable=self.criterio)
        self.ErrorButton.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # Tree Frame   
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=0, column=1, pady=10)
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        cols = ("Iteracion", "X", "Xi+1", "Ea")
        self.treeview = ttk.Treeview(tree_frame, show="headings", yscrollcommand=tree_scroll.set, columns=cols, height=13)
        self.treeview.column("Iteracion", width=100)
        self.treeview.column("X", width=100)
        self.treeview.column("Xi+1", width=100)
        self.treeview.column("Ea", width=100)
        self.treeview.pack()
        tree_scroll.config(command=self.treeview.yview)
    
    def showResult(self):
        if self.function_entry.get() == '':
            print("Error -----------")

        resultado = dataInput(self.function_entry, self.x_anterior_entry, self.x_actual_entry, self.tolerancia_entry, self.criterio)
        print(resultado)
        for col_name in resultado[0]:
            col = str(col_name)
            self.treeview.heading(col_name, text=col)
    
        for value_tuple in resultado[1:]:
            valueTuplestr = str(value_tuple)
            self.treeview.insert('', tk.END, values=valueTuplestr)

