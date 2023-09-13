"""
observador.py:
    Maneja el patrón observador de la APP.
"""


class Sujeto:
    observadores = []

    # agrego observadores a la lista de observadores:
    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self, *args):  # agrego el *args para tomar parametros
        for observador in self.observadores:
            print("El observador funciona")
            observador.update(args)
            # la acción la realizo dentro de observador concreto A


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        # guardo el objeto que le estoy pasando:
        self.observado_a = obj
        # de ese objeto agrego al observador a la lista de observadores:
        self.observado_a.agregar(self)

    # realizo la acción al observar un objeto:
    def update(self, *args):
        print("Los parámetros ingresados son: ", args)
