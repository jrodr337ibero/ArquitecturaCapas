from flask import Flask
from capa_presentacion.tarea_controller import tarea_bp
import sqlite3
from config import DATABASE

app = Flask(__name__)
app.register_blueprint(tarea_bp, url_prefix='/tareas')

#@app.before_first_request
def inicializar_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS tareas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, descripcion TEXT, completada BOOLEAN)')
    conn.close()

if __name__ == '__main__':
    inicializar_db()
    app.run(debug=True)
