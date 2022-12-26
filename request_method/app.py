#  Es un objeto que contiene toda la data enviada desde el cliente (pagina web)
#  al servidor. La data se obtiene utilizando los metodos POST y GEt.
# Post se espera que los inputs del usuario sean recibidos por comandos o  una
# solicitud http
# Get: La data se recopila directamente sin la necesidad de ser recibida 
# por comandos o solicitudes http

# Ojetos asociados con request: Form, cookies, Args, Files, Method

# Se importan los modulos necesarios.
from flask import Flask, render_template, request
app = Flask(__name__)


#  se crea la ruta principal
@app.route('/')
def input():
    return render_template('temp.html')

# otra ruta. 
# enlace del sitio web
@app.route('/passing', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        result = request.form

        # se envian la data(de result) para resul_data.html
        return render_template('result_data.html', result=result)

# Utilizacion de metodo GET
# la url debe ser: localhost:5000?name=Ivan
@app.route('/hello')
def hello_name():
    name = request.args.get('name')
    return f"<h2> hola que tal {name} </h2>"

# la url debe ser: localhost:5000/Ivan
@app.route('/hello')
@app.route('/hello2/<name>')
def hello_name2(name):
    return f"hey amigo {name}"


if __name__ == '__main__':
    app.run(debug=True)
