from flask import Blueprint, render_template, request, redirect, url_for
from capa_negocio.tarea_service import TareaService

tarea_bp = Blueprint('tarea', __name__)

@tarea_bp.route('/')
def listar_tareas():
    tareas = TareaService.obtener_tareas()
    return render_template('tareas.html', tareas=tareas)

@tarea_bp.route('/crear', methods=['POST'])
def crear_tarea():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    TareaService.crear_tarea(titulo, descripcion)
    return redirect(url_for('tarea.listar_tareas'))

@tarea_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_tarea(id):
    completada = request.form.get('completada') == 'on'
    TareaService.actualizar_tarea(id, completada)
    return redirect(url_for('tarea.listar_tareas'))

@tarea_bp.route('/eliminar/<int:id>')
def eliminar_tarea(id):
    TareaService.eliminar_tarea(id)
    return redirect(url_for('tarea.listar_tareas'))
