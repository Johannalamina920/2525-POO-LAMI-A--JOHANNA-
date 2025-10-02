import tkinter as tk
from tkinter import messagebox

class ListaTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - Semana 15")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry_tarea = tk.Entry(root, width=30)
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea)  # Evento tecla Enter

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack()

        self.btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.completar_tarea)
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Evento adicional: doble clic para marcar como completada
        self.listbox.bind("<Double-1>", self.completar_tarea)

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.listbox.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

    def completar_tarea(self, event=None):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.listbox.get(index)
            if not tarea.startswith("✔ "):
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + tarea)  # Marcar con símbolo
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla.")

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion)
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

# Ejecución principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()