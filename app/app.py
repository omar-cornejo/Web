from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define el modelo para almacenar los datos del formulario
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener datos del formulario
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Verificar si se recibieron todos los datos
    if not all([name, email, message]):
        return "Error: missing data", 400

    # Guardar en la base de datos
    new_submission = Submission(name=name, email=email, message=message)
    db.session.add(new_submission)
    db.session.commit()

    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)