import tkinter as tk
from tkinter import ttk

def agregar():
    texto = entry.get().strip()
    if texto:
        lista.insert('', 'end', values=(texto,))
        entry.delete(0, tk.END)

def limpiar():
    seleccion = lista.selection()
    if seleccion:
        for item in seleccion:
            lista.delete(item)
    else:
        entry.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta y campo de texto
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# Lista (Treeview para mostrar datos)
lista = ttk.Treeview(ventana, columns=("Dato",), show="headings", height=8)
lista.heading("Dato", text="Dato ingresado")
lista.pack(pady=10, fill="both", expand=True)

ventana.mainloop()