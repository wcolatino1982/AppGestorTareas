from flask import Flask, render_template, request, redirect, url_for, flash
import db
from models import Tarea
from datetime import datetime as dt
import sqlalchemy

# -- settings servidor --
app = Flask(__name__)  # Servidor web Flask en app
app.secret_key = 'mysecretkey'


@app.route('/')  # pagina home
def home():
    busca = db.session.query(Tarea)
    ordenar = sqlalchemy.sql.expression.asc(Tarea.fecha)
    todas_las_tareas = busca.order_by(ordenar)
    return render_template("index.html", lista_de_tareas=todas_las_tareas)
    # https://www.adamsmith.haus/python/answers/how-to-order-by-desc-in-sqlalchemy-in-python

@app.route('/crear-tarea', methods=['POST'])
def crear():
    #tarea es un objeto de la clase Tarea()
    try:
        fechaLimite = dt.strptime(request.form['fecha_limite'], '%Y-%m-%d').date()
    except ValueError:
        fechaLimite = dt.now().date()
    tarea = Tarea(contenido=request.form['contenido_tarea'].upper(),
                  categoria=request.form['contenido_categoria'].upper(),
                  fecha=fechaLimite,
                  hecha=False)
    db.session.add(tarea) # añadir el objeto de Tarea a la base de datos
    db.session.commit() # ejecuta la operación pendiente de la base de datos
    return redirect(url_for('home'))
    #db.session.close()


@app.route('/editar-tarea/<id>')
def get_tarea(id):
    tarea_selecionada = db.session.query(Tarea).filter_by(id=(id))
    return render_template('/edit.html', tarea=tarea_selecionada[0])


@app.route('/update/<id>', methods = ['POST'])
def update(id):
    try:
        fechaLimite = dt.strptime(request.form['fecha_limite'], '%Y-%m-%d').date()
    except ValueError:
        fechaLimite = dt.now().date()
    if request.method == 'POST':
        contenido = request.form['contenido_tarea'].upper()
        categoria = request.form['contenido_categoria'].upper()
        fecha = fechaLimite
        cur = db.session.query(Tarea).filter(Tarea.id == (id)).update({Tarea.contenido:contenido, Tarea.categoria:categoria, Tarea.fecha:fechaLimite})
        db.session.commit()
        flash('¡Tarea Actualizada con Éxito!')
        return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete()
    # Se busca en la base de datos por el registro cuyo id coincida
    # con el aportado por el parametro de la ruta y se elimina.
    db.session.commit() # ejecuta operaciones pendientes en el DB
    flash('¡Tarea Eliminada con Éxito!')
    return redirect(url_for('home')) # vuelve a home
    #db.session.close()  # cierra la conexion


@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for('home'))
    #db.session.close()

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)  # Se Crea el modelo de datos, es decir, las tablas
    app.run(debug=True)  # arranca, reinicia solo el servidor Flask
