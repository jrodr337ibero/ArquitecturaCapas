import sqlite3
from config import DATABASE

class Tarea:
    def __init__(self, titulo, descripcion, completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada

    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def crear_tarea(titulo, descripcion):
        conn = Tarea.get_db_connection()
        conn.execute('INSERT INTO tareas (titulo, descripcion, completada) VALUES (?, ?, ?)',
                     (titulo, descripcion, False))
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_tareas():
        conn = Tarea.get_db_connection()
        tareas = conn.execute('SELECT * FROM tareas').fetchall()
        conn.close()
        return tareas

    @staticmethod
    def actualizar_tarea(id, completada):
        conn = Tarea.get_db_connection()
        conn.execute('UPDATE tareas SET completada = ? WHERE id = ?', (completada, id))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar_tarea(id):
        conn = Tarea.get_db_connection()
        conn.execute('DELETE FROM tareas WHERE id = ?', (id,))
        conn.commit()
        conn.close()
