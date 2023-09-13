"""Este es el archivo de la Vista de acuerdo al patrón de diseño MVC. 
En este archivo se encuentra todo el código relacionado con la parte visual de la aplicación, 
los botones, los campos de entrada, la carga de la imagen de la app, etc.
Al final de este código se encuentra una sentencia del tipo try-except que larga un error si
no es posible dar de alta el producto ingresado
"""


from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import Label, StringVar, IntVar, Entry, Button
from modelo_final_leofds3 import Abmc
import os
from PIL import Image, ImageTk


class ViewVista:
    def __init__(self, master):
        self.objeto_base2 = Abmc()

        self.master = master
        self.master.geometry("500x500")
        self.master.title("Trabajo final")

        self.prenda = Label(self.master, text="Prenda")
        self.prenda.grid(row=1, column=2)
        self.modelo = Label(self.master, text="Modelo")
        self.modelo.grid(row=2, column=2)
        self.precio = Label(self.master, text="Precio")
        self.precio.grid(row=3, column=2)

        self.prenda2 = StringVar()
        self.modelo2 = StringVar()
        self.precio2 = IntVar()

        self.entry_prenda = Entry(
            self.master, textvariable=self.prenda2, width=40)
        self.entry_prenda.grid(row=1, column=3)
        self.entry_modelo = Entry(
            self.master, textvariable=self.modelo2, width=40)
        self.entry_modelo.grid(row=2, column=3)
        self.entry_precio = Entry(
            self.master, textvariable=self.precio2, width=40)
        self.entry_precio.grid(row=3, column=3)

        self.BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        #self.ruta = os.path.join(self.BASE_DIR, "IMAGE.jpg")

        #self.image1 = Image.open(self.ruta)
        #self.image2 = ImageTk.PhotoImage(self.image1)
        #self.background_label = ttk.Label(self.master, image=self.image2)
        #self.background_label.place(x=360, y=60, relwidth=0.9, relheight=1)

        self.tree = ttk.Treeview(self.master)
        self.tree["columns"] = ("Prenda", "Modelo", "Precio")
        self.tree.column("#0", width=50, minwidth=0)
        self.tree.column("Prenda", width=100, minwidth=80, anchor="s")
        self.tree.column("Modelo", width=100, minwidth=80, anchor="s")
        self.tree.column("Precio", width=100, minwidth=80, anchor="s")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Prenda", text="Prenda")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Precio", text="Precio")
        self.tree.rowconfigure(10, weight=2)
        self.tree.grid(row=20, column=2, columnspan=10)

        self.boton_g = Button(
            self.master,
            text="Agregar artículo",
            command=lambda: self.vista_alta(
                self.prenda2, self.modelo2, self.precio2, self.tree
            ),
        )
        self.boton_g.grid(row=4, column=3)
        self.master.bind(
            "<Return>",
            lambda event: self.vista_alta(
                self.prenda2, self.modelo2, self.precio2, self.tree
            ),
        )

        self.boton_f = Button(
            self.master,
            text="Borrar artículo",
            command=lambda: self.objeto_base2.baja(self.tree),
        )
        self.boton_f.grid(row=5, column=3)
        self.master.bind(
            "<Delete>", lambda event: self.objeto_base2.baja(self.tree))

        self.boton_h = Button(
            self.master,
            text="Modificar artículo",
            command=lambda: self.objeto_base2.modificacion(
                self.prenda2, self.modelo2, self.precio2, self.tree
            ),
        )
        self.boton_h.grid(row=6, column=3)

    def vista_alta(self, prenda2, modelo2, precio2, tree):
        try:
            self.objeto_base2.alta(prenda2, modelo2, precio2, tree)
            self.entry_prenda.focus()

        except Exception:
            showerror(
                message="El campo precio debe contener sólo NÚMEROS", title="Error"
            )
            self.precio2.set("")
