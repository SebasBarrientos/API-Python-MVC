from tkinter import Tk
import Vista
import Observador

class Controller:
    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = Vista.Tkint(self.root_controller)
        self.observer = Observador.Observador_A() 


if __name__ == '__main__':
    master = Tk()
    Controller(master)
    master.mainloop()