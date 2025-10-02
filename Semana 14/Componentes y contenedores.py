import json, os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Intentar usar DateEntry
try:
    from tkcalendar import DateEntry
    _HAS_DATEENTRY = True
except:
    DateEntry = None
    _HAS_DATEENTRY = False

FILE = "events.json"
DATE_FMT, TIME_FMT = "%Y-%m-%d", "%H:%M"

class Agenda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Personal")
        self.geometry("680x420")
        self.resizable(False, False)
        self.events = self.load()
        self.ui()

    def ui(self):
        # Treeview
        cols = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)
        for c, w in zip(cols, (100, 80, 450)):
            self.tree.heading(c, text=c)
            self.tree.column(c, width=w)
        self.tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.edit_event)

        # Entradas
        f = ttk.Frame(self)
        f.grid(row=1, column=0, columnspan=3, pady=5)
        ttk.Label(f, text="Fecha:").grid(row=0, column=0)
        self.e_date = DateEntry(f, date_pattern='yyyy-mm-dd') if _HAS_DATEENTRY else ttk.Entry(f)
        self.e_date.grid(row=0, column=1, padx=5)
        self.e_date.insert(0, datetime.now().strftime(DATE_FMT))
        ttk.Label(f, text="Hora:").grid(row=0, column=2)
        self.e_time = ttk.Entry(f, width=8)
        self.e_time.grid(row=0, column=3, padx=5)
        self.e_time.insert(0, datetime.now().strftime(TIME_FMT))
        ttk.Label(f, text="Desc:").grid(row=0, column=4)
        self.e_desc = ttk.Entry(f, width=40)
        self.e_desc.grid(row=0, column=5, padx=5)

        # Botones
        ttk.Button(self, text="Agregar", command=self.add).grid(row=2, column=0, pady=10)
        ttk.Button(self, text="Eliminar", command=self.delete).grid(row=2, column=1)
        ttk.Button(self, text="Salir", command=self.destroy).grid(row=2, column=2)

        self.refresh()

    # --- Funciones ---
    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save(self):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.events, f, ensure_ascii=False, indent=2)

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for ev in sorted(self.events, key=lambda e: (e["date"], e["time"])):
            self.tree.insert("", "end", values=(ev["date"], ev["time"], ev["description"]))

    def add(self):
        d, t, desc = self.e_date.get().strip(), self.e_time.get().strip(), self.e_desc.get().strip()
        try:
            datetime.strptime(d, DATE_FMT)
            datetime.strptime(t, TIME_FMT)
            if not desc:
                raise ValueError
        except:
            return messagebox.showwarning("Error", "Datos inválidos o incompletos.")
        self.events.append({"date": d, "time": t, "description": desc})
        self.save()
        self.refresh()
        self.e_desc.delete(0, "end")

    def delete(self):
        sel = self.tree.selection()
        if not sel:
            return
        if not messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):
            return
        vals = self.tree.item(sel[0], "values")
        self.events = [e for e in self.events if tuple(e.values()) != vals]
        self.save()
        self.refresh()

    def edit_event(self, e):
        sel = self.tree.selection()
        if not sel:
            return
        d, t, desc = self.tree.item(sel, "values")[0:3]
        new_desc = simpledialog.askstring("Editar", "Nueva descripción:", initialvalue=desc)
        if new_desc:
            for ev in self.events:
                if ev["date"] == d and ev["time"] == t and ev["description"] == desc:
                    ev["description"] = new_desc
                    break
            self.save()
            self.refresh()

if __name__ == "__main__":
    if not _HAS_DATEENTRY:
        print("Nota: Instala tkcalendar para mejor selección de fecha: pip install tkcalendar")
    Agenda().mainloop()
