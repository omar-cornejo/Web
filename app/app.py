from flask import Flask, Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])  # Ruta para procesar el formulario POST
def submit():
    # Obtener datos del formulario
    name = request.form.get('name')  # Obtener el campo "name"
    email = request.form.get('email')  # Obtener el campo "email"
    message = request.form.get('message')  # Obtener el campo "message"

    # Verificar si se recibieron todos los datos
    if not all([name, email, message]):
        return "Error: missing data", 400

    # Crear el archivo de texto para escribir los datos del formulario
    with open("submissions.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Message: {message}\n")
        f.write("-" * 20 + "\n")  # Línea para separar las entradas

    # Puedes devolver un mensaje de éxito o redirigir a otra página
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    app.run(debug=True, port=5000)