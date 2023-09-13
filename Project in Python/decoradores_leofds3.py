from datetime import datetime
import locale


def decoradoralta(func):
    def envoltura_alta(self, prenda2, modelo2, precio2, tree):
        prenda = prenda2.get()
        modelo = modelo2.get()
        precio = precio2.get()

        func(self, prenda2, modelo2, precio2, tree)
        print("Se ha realizado un alta de registro")
        # prenda = prenda2.get()
        locale.getlocale()
        ("en_US", "UTF-8")
        locale.setlocale(locale.LC_TIME, "es_ES")
        fecha_actual = datetime.now().strftime("%c")
        registro = open("log.txt", "a+")
        registro.write(
            f"{fecha_actual} - Alta de artículo: {prenda} - {modelo} - precio: ${precio}\n"
        )
        registro.close()

    return envoltura_alta


def decoradorbaja(func):
    def envoltura_baja(*args):
        func(*args)
        print("Se ha realizado una baja de registro")
        locale.getlocale()
        ("en_US", "UTF-8")
        locale.setlocale(locale.LC_TIME, "es_ES")
        fecha_actual = datetime.now().strftime("%c")
        registro = open("log.txt", "a+")
        registro.write(f"{fecha_actual} - Baja de artículo\n")
        registro.close()

    return envoltura_baja


def decoradormodif(func):
    def envoltura_modif(self, prenda2, modelo2, precio2, tree):
        func(self, prenda2, modelo2, precio2, tree)
        print("Se ha realizado una modificación de registro")
        prenda = prenda2.get()
        modelo = modelo2.get()
        precio = precio2.get()
        locale.getlocale()
        ("en_US", "UTF-8")
        locale.setlocale(locale.LC_TIME, "es_ES")
        fecha_actual = datetime.now().strftime("%c")
        registro = open("log.txt", "a+")
        registro.write(
            f"{fecha_actual} - Modificación de artículo: {prenda} - {modelo} - precio: ${precio}\n"
        )
        registro.close()

    return envoltura_modif
