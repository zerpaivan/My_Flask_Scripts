""""
flash o flashing messages
ventana emergente (pop-up) o cuadro de dialogo que se muestra en la pagina web
el cual tiene el fin de informar al usuario
"""

from flask import Flask, request, render_template, flash, url_for
app = Flask(__name__)
app.secret_key = "14gfr*8-fc21"
@app.route('/')
def index():
    numero = request.args.get("numero", None)
    if not numero:
        # mensaje flash que se muestra si el usuario no ingresa nada
        flash("introduce un numero en la url. Ejemplo: localhost:5000?numero=4")

    return render_template("messages.html", numero=numero)
if __name__ == "__main__":
    app.run(debug=True)