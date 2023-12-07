import tkinter as tk
from tkinter import ttk
import sv_ttk
from gui.NewtonGUI import  NewtonContent
from gui.BisectionGUI import BisectionContent
from gui.SecanteGUI import SecanteContent
from gui.interpolacionLinealGUI import interpolacionLinealContent
from gui.mullerGUI import mullerContent


class InterfazPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Metodos Numericos")

        sv_ttk.use_light_theme()

        self.create_widgets()

    def create_widgets(self):
      
        # Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tab #1
        NewtonTab = ttk.Frame(self.notebook)
        NewtonTabContent = NewtonContent(NewtonTab)
        NewtonTabContent.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(NewtonTab, text="Newton Raphson")

        # Tab #2
        BiseccionTab = ttk.Frame(self.notebook)
        BiseccionTabContent = BisectionContent(BiseccionTab)
        BiseccionTabContent.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(BiseccionTab, text="Biseccion")

        #Tab #3
        SecantTab = ttk.Frame(self.notebook)
        SecantTabContent = SecanteContent(SecantTab) #metodo de la secanta
        SecantTabContent.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(SecantTab, text="Secante")

        #Tab #4
        LinealInterpolationTab = ttk.Frame(self.notebook)
        LinealInterpolationTabContent = interpolacionLinealContent(LinealInterpolationTab) #Llamar al metodo de falsa posicion
        LinealInterpolationTabContent.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(LinealInterpolationTab, text="Falsa posicion")

        #Tab #5
        OtroMetodoTab = ttk.Frame(self.notebook)
        OtroMetodoTabContent = mullerContent(OtroMetodoTab) #Llamar al metodo de Newton Mejorado o Muller
        OtroMetodoTabContent.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(OtroMetodoTab, text="Müller")

if __name__ == "__main__":
    app = InterfazPrincipal()
    app.mainloop()
