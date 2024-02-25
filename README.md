# Curso-Python-UTN
Trabajo Final del proyecto de la Diplomatura en Python de la UTN

Hola! 
El objetivo de la app es generar una aplicación donde uno pueda cargar sus rutinas de entrenamiento 
en una la base de datos, dando las opciones de modificarlas y eliminarlas si es necesario.

La interfaz cuenta con 7 campos de entrada, 5 botones, 
un tree de visualización de información de la base de datos y una foto decorativa.
En la parte superior se encuentran los campos de entrada, donde uno realiza el ingreso de la información:
    1) Dias
    2 al 7) Ejercicios

5 botones que cumplen las siguientes funciones:
    Guardar: Cumple la función de guardar la información cargada en los campos en la base de datos.
    Ver Base de Datos: refresca el contenido del tree (Este botón tiene como objetivo
    demostrar mayor contenido de las clases aplicados a la entrega final, se podrá apreciar que al modificar algo aparecen carteles 
    de 'toca actualizar').
    Eliminar: Elimina el contenido del elemento seleccionado en el tree, de la base de datos.
    Modificar: Modifica los campos del elemento del tree seleccionado.
    Borrar campos de entrada: Borra los campos de los entry (es un botón útil debido a que, 
    al seleccionar un ítem del tree, se completan automáticamente los entry, 
    lo cual puede resultar molesto al tener que borrar uno por uno si se quiere modificar todo)

Cree un decorador que genera un txt donde se almacena que comportamiento se tuvo sobre la BD (si se agrego contenido, 
se modifico o se elimino) y en que hora exacta se realizo dicha accion.
Finalmente implemente un observador que toma nota de cuando se inicia la aplicacion con la hora exacta (puede resultar util para el control)




