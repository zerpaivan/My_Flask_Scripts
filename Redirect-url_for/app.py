# redirect() : se utiliza para redirigir a un usuario a otro endpoint (una url especifica)
# url_for(): se utiliza para generar la url a partir  de una funcion especificada
# ejemplos:

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def index():
    return "Hello World"

# aca con url_for se retorna la ruta del metodo index
@app.route("/start")
def start():
    return url_for("index")

# redirect permite redireccionar a la url especificada
@app.route("/google")
def go_to_google():
    return redirect("http://www.google.com")

@app.route("/post/<int:id>")
def post(id):
    return "Showing post: {}".format(id)

@app.route("/today")
def today():
    return redirect(url_for("post", id = 50))


if __name__ == "__main__":
    app.run(debug=True)