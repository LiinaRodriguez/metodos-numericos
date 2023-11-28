import tkinter as tk
from tkinter import ttk
import sv_ttk

class BisectionContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
     
        sv_ttk.use_light_theme()
        
        self.create_widgets()

    def create_widgets(self):
        
        # Widgets Frame
        widgets_frame = ttk.LabelFrame(self, text='Ingrese los datos')
        widgets_frame.grid(row=0, column=0, padx=20, pady=10)

        self.create_entry(widgets_frame, "f()")
        self.create_entry(widgets_frame, "x-1")
        self.create_entry(widgets_frame, "x")
        self.create_entry(widgets_frame, "Criterio")

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

    def create_entry(self, parent, label_text):
        function_entry = ttk.Entry(parent)
        function_label = ttk.Label(parent, text=label_text)
        function_label.grid(row=len(parent.grid_slaves()) + 1, column=0, padx=5, pady=(0, 5), sticky="ew")
        function_entry.grid(row=len(parent.grid_slaves()) + 1, column=1, padx=5, pady=5, sticky="ew")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MyApp(root)
#     root.mainloop()
