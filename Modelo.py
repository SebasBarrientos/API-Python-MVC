import sqlite3 
import re
from datetime import datetime
from Observador import Subject


def historial(funcion):
  def wrapper(*args, **kwargs):
    fecha_hora = datetime.today().strftime("%d/%m/%y %H:%M:%S")

    nombre_funcion = funcion.__name__

    datos_relevantes = ""
    if nombre_funcion == "insertar_datos":
        datos_relevantes = " - Se agrego contenido a la tabla."
    elif nombre_funcion == "modificar":
        datos_relevantes = " - Se modifico el contenido de la tabla"
    else:
        datos_relevantes = " - Se elimino contenido de la tabla"

    mensaje = f"{fecha_hora} - {datos_relevantes}\n"

    with open("historial_bd.txt", "a") as archivo:
      archivo.write(mensaje)

    funcion(*args, **kwargs)

  return wrapper

class Metodos_SQL(Subject):
    def __init__(self,):
        self.con = sqlite3.connect("Ejercicios_Calistenia.db")
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS ejercicios 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                dias VARCHAR(120),
                ejercicio1 VARCHAR(120),
                ejercicio2 VARCHAR(120),
                ejercicio3 VARCHAR(120),
                ejercicio4 VARCHAR(120),
                ejercicio5 VARCHAR(120),
                ejercicio6 VARCHAR(120))
        """
        cursor.execute(sql)
        self.con.commit()
    @historial
    def insertar_datos(self, var_dias, var_ejercicio1, var_ejercicio2, var_ejercicio3,
            var_ejercicio4, var_ejercicio5, var_ejercicio6,tree):
        patron="^^[A-Za-záéíóú\s]*$" 
        patron1="^[A-Za-záéíóú\s]*$"
        dias = var_dias.get()
        ejercicio1 = var_ejercicio1.get()
        ejercicio2 = var_ejercicio2.get()
        ejercicio3 = var_ejercicio3.get()
        ejercicio4 = var_ejercicio4.get()
        ejercicio5 = var_ejercicio5.get()
        ejercicio6 = var_ejercicio6.get()
        if(
            re.match(patron, dias) and 
            re.match(patron1, ejercicio1) and 
            re.match(patron1, ejercicio2) and 
            re.match(patron1, ejercicio3) and 
            re.match(patron1, ejercicio4) and 
            re.match(patron1, ejercicio5) and 
            re.match(patron1, ejercicio6)): 

            cursor=self.con.cursor()
            data=(dias, ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5, ejercicio6)
            sql='''INSERT INTO ejercicios
            (dias, 
            ejercicio1, 
            ejercicio2, 
            ejercicio3, 
            ejercicio4, 
            ejercicio5, 
            ejercicio6)
            VALUES(?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql, data)
            self.con.commit()
            self.actualizar_treeview(tree)
            self.limpiar_campos(var_dias, var_ejercicio1, var_ejercicio2,
                var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6)
            self.notify_observers
        else:
            self.mensaje_error()
    @historial
    def eliminar_datos (self,tree):
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item['text']

        cursor = self.con.cursor()
        data = (mi_id,)
        borrar = '''DELETE FROM ejercicios WHERE ID = ?;'''
        cursor.execute(borrar, data)
        self.con.commit()
        tree.delete(valor)
        self.notify_observers
    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        db = "SELECT * FROM ejercicios ORDER BY id ASC"

        cursor=self.con.cursor()
        datos=cursor.execute(db)
        resultado = datos.fetchall()
        for fila in resultado:
            mitreview.insert(
            "", 'end', text=fila[0], values= 
            (fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]
            ))
    @historial
    def modificar(self, var_dias, var_ejercicio1, var_ejercicio2, var_ejercicio3,
            var_ejercicio4, var_ejercicio5, var_ejercicio6, tree):
        dias = var_dias.get()
        ejercicio1 = var_ejercicio1.get()
        ejercicio2 = var_ejercicio2.get()
        ejercicio3 = var_ejercicio3.get()
        ejercicio4 = var_ejercicio4.get()
        ejercicio5 = var_ejercicio5.get()
        ejercicio6 = var_ejercicio6.get()
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item['text']
        patron="^[A-Za-záéíóú\s]*$" 
        patron1="^[A-Za-záéíóú\s]*$"
        if(
            re.match(patron, dias) and 
            re.match(patron1, ejercicio1) and 
            re.match(patron1, ejercicio2) and 
            re.match(patron1, ejercicio3) and 
            re.match(patron1, ejercicio4) and 
            re.match(patron1, ejercicio5) and 
            re.match(patron1, ejercicio6)): 
            
            cursor = self.con.cursor()
            data = (dias, ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5,
                ejercicio6, mi_id)
            mod = '''UPDATE ejercicios
            SET dias = ?,
                ejercicio1 = ?,
                ejercicio2 = ?,
                ejercicio3 = ?,
                ejercicio4 = ?,
                ejercicio5 = ?,
                ejercicio6 = ?
                WHERE id = ?
            '''
            cursor.execute(mod,data)
            self.mensaje_actualiza()
            self.con.commit()
            self.limpiar_campos(var_dias, var_ejercicio1, var_ejercicio2,
                var_ejercicio3, var_ejercicio4, var_ejercicio5, var_ejercicio6)
            self.notify_observers
        else:
            self.mensaje_error()

    def limpiar_campos(self, var_dias, var_ejercicio1, var_ejercicio2, var_ejercicio3,
            var_ejercicio4, var_ejercicio5, var_ejercicio6):
        var_dias.set("")
        var_ejercicio1.set("")
        var_ejercicio2.set("")
        var_ejercicio3.set("")
        var_ejercicio4.set("")
        var_ejercicio5.set("")
        var_ejercicio6.set("")

    def llenar_campos(self, tree, var_dias, var_ejercicio1, var_ejercicio2, var_ejercicio3,
            var_ejercicio4, var_ejercicio5, var_ejercicio6):
        item = tree.selection()
        if item:
            mi_id = item[0]
            valores = tree.item(mi_id, 'values')

            var_dias.set(valores[0])
            var_ejercicio1.set(valores[1])
            var_ejercicio2.set(valores[2])
            var_ejercicio3.set(valores[3])
            var_ejercicio4.set(valores[4])
            var_ejercicio5.set(valores[5])
            var_ejercicio6.set(valores[6])
