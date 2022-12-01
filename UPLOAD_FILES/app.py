import os
# Creacion de Servidor
from flask import Flask
from flask import render_template, request, flash, redirect
from werkzeug.utils import secure_filename 

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'git'}
app = Flask(__name__)
app.secret_key = "secret key" # es requerido por el comando flash

# funcion para verificar si el archivo esta permitido
# separa la extension del nombre del archivo con rsplit()
def allowed_file(filename:str):
    if '.' in filename:
        extension = filename.rsplit('.', 1)[1].lower()
        if extension in ALLOWED_EXTENSIONS:
            return True
        else:
            return False
    else:
        return False


@app.route('/') # cargar form
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    # verifica que form tiene un "file_to_upload"
    if 'file_to_upload' not in request.files: 
        flash('Not file part')
        return redirect(request.url)

    file = request.files['file_to_upload']
    
    # verifica si se a seleccionado un archivo
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    
    # verifica que la extension es la permitida y  asegura el 
    # nombre del archivo con secure_filename. NUNCA CONFIES EN EL USUARIO
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)



if __name__== '__main__':
    app.run(debug=True)