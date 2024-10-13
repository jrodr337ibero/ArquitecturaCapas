from capa_datos.tareadb import Tarea

class TareaService:
    @staticmethod
    def crear_tarea(titulo, descripcion):
        Tarea.crear_tarea(titulo, descripcion)

    @staticmethod
    def obtener_tareas():
        return Tarea.obtener_tareas()

    @staticmethod
    def actualizar_tarea(id, completada):
        Tarea.actualizar_tarea(id, completada)

    @staticmethod
    def eliminar_tarea(id):
        Tarea.eliminar_tarea(id)
