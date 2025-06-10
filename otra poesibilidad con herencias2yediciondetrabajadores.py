import tkinter as tk
from tkinter import ttk, messagebox

# === Clases con herencia ===

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class PersonalHospital:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.ocupado = False

class Doctor(PersonalHospital):
    pass

class Enfermero(PersonalHospital):
    pass

class Paciente(Persona):
    def __init__(self, nombre, edad, area, camilla, doctor, enfermero):
        super().__init__(nombre, edad)
        self.area = area
        self.camilla = camilla
        self.doctor = doctor
        self.enfermero = enfermero

# === Datos iniciales ===

doctores = [
    Doctor("Dr. Pérez", "Urgencias"),
    Doctor("Dr. Gómez", "Hospitalización"),
]

enfermeros = [
    Enfermero("Enf. Martínez", "Urgencias"),
    Enfermero("Enf. López", "Hospitalización"),
]

camillas = {
    "Urgencias": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(3)],
    "Hospitalización": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
}

pacientes = []

# === Funciones ===

def asignar_camilla(area):
    for i, camilla in enumerate(camillas[area]):
        if not camilla["ocupada"]:
            doc = next((d for d in doctores if d.area == area and not d.ocupado), None)
            enf = next((e for e in enfermeros if e.area == area and not e.ocupado), None)

            if doc is None or enf is None:
                return None, None, None

            camilla["ocupada"] = True
            camilla["doctor"] = doc
            camilla["enfermero"] = enf
            doc.ocupado = True
            enf.ocupado = True
            return i + 1, doc, enf
    return None, None, None

def registrar_paciente():
    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    area = combo_area.get().strip()

    if not nombre or not edad or not area:
        messagebox.showerror("Error", "Complete todos los campos")
        return
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "Edad debe ser un número")
        return

    camilla_num, doc, enf = asignar_camilla(area)
    if camilla_num is None:
        messagebox.showerror("Error", f"No hay camillas o personal disponible en {area}")
        return

    paciente = Paciente(nombre, edad, area, camilla_num, doc, enf)
    pacientes.append(paciente)
    messagebox.showinfo("Éxito", f"Paciente registrado en camilla {camilla_num} de {area}")

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

def mostrar_pacientes():
    ventana = tk.Toplevel()
    ventana.title("Pacientes")

    cols = ("Nombre", "Edad", "Área", "Camilla", "Doctor", "Enfermero")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for p in pacientes:
        tree.insert("", tk.END, values=(
            p.nombre,
            p.edad,
            p.area,
            p.camilla,
            p.doctor.nombre if p.doctor else "N/A",
            p.enfermero.nombre if p.enfermero else "N/A"
        ))

    tree.pack(expand=True, fill=tk.BOTH)

def mostrar_personal():
    ventana = tk.Toplevel()
    ventana.title("Personal")

    cols = ("Nombre", "Área", "Tipo", "Ocupado")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for d in doctores:
        tree.insert("", tk.END, values=(d.nombre, d.area, "Doctor", "Sí" if d.ocupado else "No"))
    for e in enfermeros:
        tree.insert("", tk.END, values=(e.nombre, e.area, "Enfermero", "Sí" if e.ocupado else "No"))

    tree.pack(expand=True, fill=tk.BOTH)

    def editar_personal():
        try:
            item = tree.selection()[0]
            nombre = tree.item(item, 'values')[0]
            tipo = tree.item(item, 'values')[2]

            personal = next((p for p in (doctores if tipo == "Doctor" else enfermeros) if p.nombre == nombre), None)

            ventana_editar = tk.Toplevel()
            ventana_editar.title("Editar Personal")
            ventana_editar.lift()

            tk.Label(ventana_editar, text="Nombre:").grid(row=0, column=0)
            entry_nombre_ed = tk.Entry(ventana_editar)
            entry_nombre_ed.insert(0, personal.nombre)
            entry_nombre_ed.grid(row=0, column=1)

            tk.Label(ventana_editar, text="Área:").grid(row=1, column=0)
            combo_area_ed = ttk.Combobox(ventana_editar, values=list(camillas.keys()), state="readonly")
            combo_area_ed.set(personal.area)
            combo_area_ed.grid(row=1, column=1)

            def guardar_edicion():
                personal.nombre = entry_nombre_ed.get().strip()
                personal.area = combo_area_ed.get().strip()
                messagebox.showinfo("Éxito", f"{tipo} actualizado correctamente.")
                ventana_editar.destroy()
                ventana.destroy()
                mostrar_personal()

            tk.Button(ventana_editar, text="Guardar", command=guardar_edicion).grid(row=2, column=0, columnspan=2)

        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un personal para editar.")

    def eliminar_personal():
        try:
            item = tree.selection()[0]
            nombre = tree.item(item, 'values')[0]
            tipo = tree.item(item, 'values')[2]

            if tipo == "Doctor":
                doctores[:] = [d for d in doctores if d.nombre != nombre]
            else:
                enfermeros[:] = [e for e in enfermeros if e.nombre != nombre]

            messagebox.showinfo("Éxito", f"{tipo} eliminado correctamente.")
            ventana.destroy()
            mostrar_personal()

        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un personal para eliminar.")

    tk.Button(ventana, text="Editar", command=editar_personal).pack(side=tk.LEFT, padx=10)
    tk.Button(ventana, text="Eliminar", command=eliminar_personal).pack(side=tk.LEFT, padx=10)

def registrar_doctor():
    def guardar_doctor():
        nombre = entry_nombre.get().strip()
        area = combo_area.get().strip()

        if not nombre or not area:
            messagebox.showerror("Error", "Complete todos los campos")
            return

        doctores.append(Doctor(nombre, area))
        messagebox.showinfo("Éxito", f"Doctor {nombre} registrado.")
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title("Registrar Doctor")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Área:").grid(row=1, column=0)
    combo_area = ttk.Combobox(ventana, values=list(camillas.keys()), state="readonly")
    combo_area.grid(row=1, column=1)

    tk.Button(ventana, text="Guardar", command=guardar_doctor).grid(row=2, column=0, columnspan=2)

def registrar_enfermero():
    def guardar_enfermero():
        nombre = entry_nombre.get().strip()
        area = combo_area.get().strip()

        if not nombre or not area:
            messagebox.showerror("Error", "Complete todos los campos")
            return

        enfermeros.append(Enfermero(nombre, area))
        messagebox.showinfo("Éxito", f"Enfermero/a {nombre} registrado/a.")
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title("Registrar Enfermero")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Área:").grid(row=1, column=0)
    combo_area = ttk.Combobox(ventana, values=list(camillas.keys()), state="readonly")
    combo_area.grid(row=1, column=1)

    tk.Button(ventana, text="Guardar", command=guardar_enfermero).grid(row=2, column=0, columnspan=2)

# === Interfaz gráfica principal ===

ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital")

tk.Label(ventanaprincipal, text="Nombre Paciente:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventanaprincipal)
entry_nombre.grid(row=0, column=1)

tk.Label(ventanaprincipal, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(ventanaprincipal)
entry_edad.grid(row=1, column=1)

tk.Label(ventanaprincipal, text="Área:").grid(row=2, column=0)
combo_area = ttk.Combobox(ventanaprincipal, values=list(camillas.keys()), state="readonly")
combo_area.grid(row=2, column=1)

tk.Button(ventanaprincipal, text="Registrar Paciente", command=registrar_paciente).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(ventanaprincipal, text="Mostrar Pacientes", command=mostrar_pacientes).grid(row=4, column=0, sticky="ew", padx=5, pady=2)
tk.Button(ventanaprincipal, text="Administrar Personal", command=mostrar_personal).grid(row=4, column=1, sticky="ew", padx=5, pady=2)
tk.Button(ventanaprincipal, text="Registrar Doctor", command=registrar_doctor).grid(row=5, column=0, sticky="ew", padx=5, pady=2)
tk.Button(ventanaprincipal, text="Registrar Enfermero", command=registrar_enfermero).grid(row=5, column=1, sticky="ew", padx=5, pady=2)

ventanaprincipal.mainloop()
