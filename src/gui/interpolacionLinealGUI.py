import tkinter as tk
from tkinter import ttk
import sv_ttk
from metodosNumericos.interpolacionLineal import dataInput
from tkinter import BooleanVar, messagebox

class interpolacionLinealContent(tk.Frame):
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

        self.xl_entry = ttk.Entry(self.inputFrame)
        self.xl_label = ttk.Label(self.inputFrame, text='xl')
        self.xl_label.grid(row=1,column=0,padx=5, pady=(0, 5), sticky="ew")
        self.xl_entry.grid(row=1,column=1, padx=5, pady=5, sticky="ew")

        self.xu_entry = ttk.Entry(self.inputFrame)
        self.xu_label = ttk.Label(self.inputFrame, text="xi")
        self.xu_label.grid(row=2,column=0,padx=5, pady=(0, 5), sticky="ew")
        self.xu_entry.grid(row=2,column=1, padx=5, pady=5, sticky="ew")

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

        cols = ("Iteracion", "xl", "f(xl)", "xu", "f(xu)", "xr", "Ea")
        self.treeview = ttk.Treeview(tree_frame, show="headings", yscrollcommand=tree_scroll.set, columns=cols, height=13)
        self.treeview.column("Iteracion", width=90)
        self.treeview.column("xl", width=60)
        self.treeview.column("f(xl)", width=60)
        self.treeview.column("xu", width=60)
        self.treeview.column("f(xu)", width=60)
        self.treeview.column("xr", width=60)
        self.treeview.column("Ea", width=60)
        self.treeview.pack()
        tree_scroll.config(command=self.treeview.yview)

    
    def showResult(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        if any([
        self.function_entry.get() == '',
        self.x1_entry.get() == '',
        self.x2_entry.get() == '',
        self.x3_entry.get() == '',
        self.tolerancia_entry.get() == '',
        ]):
            messagebox.showwarning("Error", "Por favor ingrese los datos.")
            return

        resultado = dataInput(self.function_entry, self.xl_entry, self.xu_entry, self.tolerancia_entry, self.criterio)
        print(resultado)
        for col_name in resultado[0]:
            col = str(col_name)
            self.treeview.heading(col_name, text=col)
    
        for value_tuple in resultado[1:]:
            valueTuplestr = str(value_tuple)
            self.treeview.insert('', tk.END, values=valueTuplestr)

