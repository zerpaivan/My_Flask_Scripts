import os
# Creacion de Servidor
from flask import Flask
from flask import render_template, request, flash, redirect
from werkzeug.utils import secure_filename 

UPLOAD_FOLDER = 'static/uploads/' # carpeta donde se cargan los archivos

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'git'} # Extensiones permitidas
app = Flask(__name__)
app.secret_key = "secret key" # es requerido por el comando flash
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16megas max tamaño del archivo

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
    # print(file)
    # verifica si se a seleccionado un archivo
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    
    # verifica que la extension es la permitida y  asegura el 
    # nombre del archivo con secure_filename. NUNCA CONFIES EN EL USUARIO
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image_filename: ', filename)
        flash('image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are: png, jpg, jpeg, git')
        return redirect(request.url)


if __name__== '__main__':
    app.run(debug=True)