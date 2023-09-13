"""Este es el archivo del Controlador de acuerdo al patrón de diseño MVC. Ejecuta la ventana de Tkinter 
y actualiza el treeview de la app para que al abrir la app ésta ya se encuentre con su treeview cargado.
"""

from tkinter import Tk
from vista_final_leofds3 import ViewVista
import observador_leofds3


class Controlador1:
    def __init__(self, master):
        self.master_controlador = master
        self.objeto_view = ViewVista(self.master_controlador)
        self.objeto_view.objeto_base2.actualizar_treeview(
            self.objeto_view.tree)
        self.objeto_view.entry_prenda.focus()
        self.el_observador = observador_leofds3.ConcreteObserverA(
            self.objeto_view.objeto_base2)


if __name__ == "__main__":
    leo_fd = Tk()
    app = Controlador1(leo_fd)
    leo_fd.mainloop()
