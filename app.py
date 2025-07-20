from flask import Flask, render_template, request, redirect, url_for
import mysql.connector  
import os  
from werkzeug.utils import secure_filename  

app = Flask(__name__)

# subir imágenes
UPLOAD_FOLDER = os.path.join('static', 'uploads')  
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# funcion bd
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='futbol_utp'
    )

@app.route('/')
def listar_jugadores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jugadores")  
    jugadores = cursor.fetchall()  
    conn.close()
    return render_template('jugadores/index.html', jugadores=jugadores)

# Mostrar formulario 
@app.route('/jugadores/nuevo')
def nuevo_jugador():
    return render_template('jugadores/nuevo.html')

# Guardar jugador bd
@app.route('/jugadores/guardar', methods=['POST'])
def guardar_jugador():
    nombre = request.form['nombre']
    posicion = request.form['posicion']
    numero = request.form['numero']
    edad = request.form['edad']
    nacionalidad = request.form['nacionalidad']

    # Guardar image
    foto = request.files['foto']
    filename = None
    if foto and allowed_file(foto.filename):
        filename = secure_filename(foto.filename)  
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  

    # Insertar en la bd
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jugadores (nombre, posicion, numero, edad, nacionalidad, foto)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, posicion, numero, edad, nacionalidad, filename))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_jugadores'))  

# Mostrar formulario para editar 
@app.route('/jugadores/editar/<int:id>')
def editar_jugador(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jugadores WHERE id = %s", (id,))
    jugador = cursor.fetchone()  
    conn.close()
    return render_template('jugadores/editar.html', jugador=jugador)

#  Actualizar un jugador bd
@app.route('/jugadores/actualizar/<int:id>', methods=['POST'])
def actualizar_jugador(id):
    nombre = request.form['nombre']
    posicion = request.form['posicion']
    numero = request.form['numero']
    edad = request.form['edad']
    nacionalidad = request.form['nacionalidad']
    foto = request.files.get('foto')
    filename = None

    conn = get_connection()
    cursor = conn.cursor()

    if foto and allowed_file(foto.filename):
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Actualizar con nueva foto
        cursor.execute("""
            UPDATE jugadores SET nombre=%s, posicion=%s, numero=%s, edad=%s, nacionalidad=%s, foto=%s
            WHERE id=%s
        """, (nombre, posicion, numero, edad, nacionalidad, filename, id))
    else:
        # Actualizar sin cambiar la foto
        cursor.execute("""
            UPDATE jugadores SET nombre=%s, posicion=%s, numero=%s, edad=%s, nacionalidad=%s
            WHERE id=%s
        """, (nombre, posicion, numero, edad, nacionalidad, id))

    conn.commit()
    conn.close()
    return redirect(url_for('listar_jugadores'))

@app.route('/jugadores/eliminar/<int:id>')
def eliminar_jugador(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jugadores WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_jugadores'))

@app.route('/inicio')
def home():
    return render_template('home.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow}

# ▶️ Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

