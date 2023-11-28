import tkinter as tk
import sv_ttk

def navigate_to(page_name):
    # Función de ejemplo para la navegación
    print(f"Navegando a {page_name}")

# Función para cambiar el contenido del marco principal
def change_content(content):
    main_content.config(text=content)

# Crear la ventana principal
root = tk.Tk()
root.title("Barra de Navegación tipo Navbar")
sv_ttk.set_theme("dark")
# Crear un Frame para la barra de navegación
navbar_frame = tk.Frame(root, bg="gray", padx=10, pady=5)
navbar_frame.grid(row=0, column=0, sticky="ew")

# Crear botones de navegación y asociar cada uno a un Frame diferente
buttons = [
    {"text": "Inicio", "command": lambda: change_content("Contenido de la página de inicio")},
    {"text": "Productos", "command": lambda: change_content("Contenido de la página de productos")},
    {"text": "Servicios", "command": lambda: change_content("Contenido de la página de servicios")},
    {"text": "Contacto", "command": lambda: change_content("Contenido de la página de contacto")},
]

for index, button_data in enumerate(buttons):
    button = tk.Button(navbar_frame, text=button_data["text"], command=lambda b=button_data["text"]: change_content(b))
    button.grid(row=0, column=index, padx=5)

# Contenido de la página principal (puede ser un Frame diferente para cada página)
main_content = tk.Label(root, text="Contenido de la página de inicio", padx=10, pady=10)
main_content.grid(row=1, column=0, sticky="nsew")

# Configurar el peso de las filas y columnas para que se expandan con la ventana
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar el bucle principal de la aplicación
root.mainloop()
