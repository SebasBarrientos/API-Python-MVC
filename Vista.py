from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
import os
from PIL import ImageTk, Image
from tkinter.messagebox import showerror
from Modelo import Metodos_SQL





class Tkint(Metodos_SQL):
    def __init__(self,master):
        super().__init__()
        master.title("Calistenia")

        color_fondo = "#333333"  # Color de fondo
        color_titulos = "#0056b3"   # Color para los títulos
        color_botones = "#0056b3"  # Color para los botones
        master.configure(bg=color_fondo) 

        #------------------ VARIABLES
        var_dias = StringVar ()
        var_ejercicio1 = StringVar ()
        var_ejercicio2 = StringVar ()
        var_ejercicio3 = StringVar ()
        var_ejercicio4 = StringVar ()
        var_ejercicio5 = StringVar ()
        var_ejercicio6 = StringVar ()
        w_ancho = 30
        #-------------------------------- LABEL --------------------------------
        Dias = Label (master, text= "Dias",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', borderwidth=5, 
            relief="ridge")
        Dias.grid (row= 0, column = 1)
        Ejercicio1 = Label (master, text= "Ejercicio 1",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white',
            borderwidth=5, relief="ridge")
        Ejercicio1.grid (row= 1, column = 1)
        Ejercicio2 = Label (master, text= "Ejercicio 2",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', 
            borderwidth=5, relief="ridge")
        Ejercicio2.grid (row= 2, column = 1)
        Ejercicio3 = Label (master, text= "Ejercicio 3",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', 
            borderwidth=5, relief="ridge")
        Ejercicio3.grid (row= 3, column = 1)
        Ejercicio4 = Label (master, text= "Ejercicio 4",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', 
            borderwidth=5, relief="ridge")
        Ejercicio4.grid (row= 4, column = 1)
        Ejercicio5 = Label (master, text= "Ejercicio 5",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', 
            borderwidth=5, relief="ridge")
        Ejercicio5.grid (row= 5, column = 1)
        Ejercicio6 = Label (master, text= "Ejercicio 6",font=('Roboto', 11, "bold"), bg=color_titulos, fg ='white', 
            borderwidth=5, relief="ridge")
        Ejercicio6.grid (row= 6, column = 1)

        #-------------------------------CASILLEROS A LLENAR CON EJERCICIOS
        Dias = Entry (master, text= "Dias", textvariable= var_dias, width = w_ancho, borderwidth=5, relief="ridge")
        Dias.grid (row= 0, column =2)
        Ejercicio1 = Entry (master, text= "Ejercicio 1", textvariable= var_ejercicio1, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio1.grid (row= 1, column =2)
        Ejercicio2 = Entry (master, text= "Ejercicio 2", textvariable= var_ejercicio2, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio2.grid (row= 2, column =2)
        Ejercicio3 = Entry (master, text= "Ejercicio 3", textvariable= var_ejercicio3, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio3.grid (row= 3, column =2)
        Ejercicio4 = Entry (master, text= "Ejercicio 4", textvariable= var_ejercicio4, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio4.grid (row= 4, column =2)
        Ejercicio5 = Entry (master, text= "Ejercicio 5", textvariable= var_ejercicio5, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio5.grid (row= 5, column =2)
        Ejercicio6 = Entry (master, text= "Ejercicio 6", textvariable= var_ejercicio6, width = w_ancho, borderwidth=5, 
            relief="ridge")
        Ejercicio6.grid (row= 6, column =2)

        # Treeview para mostrar datos
        tree = ttk.Treeview(master)
        tree.grid (column=0, row=9, columnspan=7, sticky='nsew')

        tree["columns"] = ("Dias", "Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4", "Ejercicio5", "Ejercicio6")
        tree.column("#0", width=50,minwidth=50, anchor='w')
        tree.column("Dias", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio1", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio2", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio3", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio4", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio5", width=150,minwidth=80, anchor='center')
        tree.column("Ejercicio6", width=150,minwidth=80, anchor='center')

        columnas = ["Dias", "Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4", "Ejercicio5", "Ejercicio6"]
        tree.heading ("#0", text = 'ID', anchor='center')
        for col in columnas:
            tree.heading(col, text=col, anchor="center")
        tree.bind("<<TreeviewSelect>>", lambda event: self.llenar_campos(tree, var_dias, var_ejercicio1,
            var_ejercicio2, var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6))

        # Botones
        botones = [
            ("Guardar", lambda: self.insertar_datos(var_dias, var_ejercicio1,
                var_ejercicio2, var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6, tree)),
            ("Ver Base de Datos", lambda: self.actualizar_treeview(tree)),
            ("Eliminar", lambda: self.eliminar_datos(tree)),
            ("Modificar", lambda: self.modificar(var_dias, var_ejercicio1,
                var_ejercicio2, var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6, tree)),
            ("Borrar campos de entrada", lambda: self.limpiar_campos(var_dias, var_ejercicio1,
                var_ejercicio2, var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6))
        ]
        for i, (btn_text, btn_command) in enumerate(botones):
            boton = Button(master, text=btn_text, command=btn_command, font=("Helvetica", 10), bg =color_botones, 
                fg ='white', borderwidth=5, relief="ridge")
            boton.grid(row=8, column=i, padx=10, pady=10)
            
            
        #foto
        BASE_DIR = os.path.dirname((os.path.abspath(__file__))) 
        ruta = os.path.join(BASE_DIR, "Calistenica.png")

        imageruta = Image.open(ruta)  

        ancho_nuevo = imageruta.width // 3
        alto_nuevo = imageruta.height // 3
        imagen_redimensionada = imageruta.resize((ancho_nuevo, alto_nuevo))
        self.image1 = ImageTk.PhotoImage (imagen_redimensionada) 
        background_label = Label (master, image=self.image1, borderwidth=20, relief="ridge")
        background_label.grid(row=0, column=4, rowspan=7)
            

    #----------------------------MEnsaje emergente------------------------------------
    def mensaje_error(self):
        showerror("Los caracteres no son validos", "Recuerda: En dias solo se admiten letras, en ejercicios se admiten letras y numeros")
    def mensaje_actualiza(self):
        showerror("Actualizar", "Toca 'Ver Base de Datos' para ver los cambios")

