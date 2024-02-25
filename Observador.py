from datetime import datetime

class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, **kwargs):
        for observer in self.observers:
            observer.update(**kwargs)


class Observer:
    def update(self, **kwargs):
        raise NotImplementedError("Delegation of update()")


class Observador_A(Observer, Subject):
    def __init__(self):
        super().__init__()
        self.record()

    def record(self):
        fecha_hora = datetime.today().strftime("%d/%m/%y %H:%M:%S")
        mensaje = f"{fecha_hora} - Se inicio programa\n"

        with open("historial_observador.txt", "a") as archivo:
            archivo.write(mensaje)