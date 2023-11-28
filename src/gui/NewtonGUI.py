import tkinter as tk
from tkinter import ttk
import sv_ttk
from newtonRapson import dataInput
from texttable import Texttable

class NewtonContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
   
        sv_ttk.use_light_theme()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Widgets Frame
        inputFrame = ttk.LabelFrame(self, text='Ingrese los datos')
        inputFrame.grid(row=0, column=0, padx=20, pady=10)

        function_entry = ttk.Entry(inputFrame)
        function_label = ttk.Label(inputFrame, text='f(x)')
        function_label.grid(row=0,column=0, padx=5, pady=(0, 5), sticky="ew")
        function_entry.grid(row=0,column=1, padx=5, pady=5, sticky="ew")

        x_anterior_entry = ttk.Entry(inputFrame)
        x_anterior_label = ttk.Label(inputFrame, text='xᵢ₋₁')
        x_anterior_label.grid(row=1,column=0,padx=5, pady=(0, 5), sticky="ew")
        x_anterior_entry.grid(row=1,column=1, padx=5, pady=5, sticky="ew")

        x_actual_entry = ttk.Entry(inputFrame)
        x_actual_label = ttk.Label(inputFrame, text="xᵢ")
        x_actual_label.grid(row=2,column=0,padx=5, pady=(0, 5), sticky="ew")
        x_actual_entry.grid(row=2,column=1, padx=5, pady=5, sticky="ew")

        tolerancia_entry = ttk.Entry(inputFrame)
        tolerancia_label = ttk.Label(inputFrame, text='Criterio')
        tolerancia_label.grid(row=3,column=0,padx=5, pady=(0, 5), sticky="ew")
        tolerancia_entry.grid(row=3,column=1, padx=5, pady=5, sticky="ew")
        
        dataInput(function_entry, x_anterior_entry, x_actual_entry, tolerancia_entry)
        
        # Tree Frame   
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=0, column=1, pady=10)
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        cols = ("Iteracion", "x", "Xi+1", "Ea")
        self.treeview = ttk.Treeview(tree_frame, show="headings", yscrollcommand=tree_scroll.set, columns=cols, height=13)
        self.treeview.column("Iteracion", width=100)
        self.treeview.column("x", width=100)
        self.treeview.column("Xi+1", width=100)
        self.treeview.column("Ea", width=100)
        self.treeview.pack()
        tree_scroll.config(command=self.treeview.yview)
    
    def showResult():
        pass
