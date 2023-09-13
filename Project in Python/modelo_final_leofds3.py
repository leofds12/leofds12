"""Este es el archivo del Modelo de acuerdo al patrón de diseño MVC.
Cuenta con una clase Abmc en la cual se encuentran todas las operaciones
relacionadas al CRUD de datos y otra clase llamada Validate2 donde se 
realiza la validación del campo de precio, de manera que
sólo se puedan ingresar datos numéricos"""

from decoradores_leofds3 import decoradoralta, decoradorbaja, decoradormodif
from bd_final_leofds3 import Venta
import re
from observador_leofds3 import Sujeto


class Abmc(Sujeto):
    def __init__(
        self,
    ):
        pass

    @decoradoralta
    def alta(self, prenda2, modelo2, precio2, tree):
        self.ventas = Venta()
        self.ventas.prenda = prenda2.get()
        self.ventas.modelo = modelo2.get()
        self.ventas.precio = precio2.get()
        self.obj_validate = Validate2()
        self.obj_validate.validation2(self.ventas.precio)
        self.ventas.save()
        self.actualizar_treeview(tree)
        self.notificar(self.ventas.prenda,
                       self.ventas.modelo, self.ventas.precio)
        prenda2.set("")
        modelo2.set("")
        precio2.set("")

    @decoradorbaja
    def baja(self, tree):
        self.ventas = Venta()
        valor = tree.selection()
        item = tree.item(valor)
        borrar = self.ventas.get(Venta.id == item["text"])
        borrar.delete_instance()
        self.actualizar_treeview(tree)

    @decoradormodif
    def modificacion(self, prenda2, modelo2, precio2, tree):
        valor = tree.selection()
        item = tree.item(valor)
        actualizar = Venta.update(
            prenda=prenda2.get(), modelo=modelo2.get(), precio=precio2.get()
        ).where(Venta.id == item["text"])
        actualizar.execute()
        self.actualizar_treeview(tree)

    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        for fila in Venta.select():
            mitreview.insert(
                "", 0, text=fila.id, values=(fila.prenda, fila.modelo, fila.precio)
            )


class Validate2:
    def validation2(self, b):
        patron = "^\\d+$"
        if re.match(patron, str(b)):
            pass
