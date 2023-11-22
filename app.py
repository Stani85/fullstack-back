""" app pizza """
from flask import Flask, request, redirect
import persistencia
import utils

app = Flask(__name__)
@app.route("/pizza", methods=['POST'])
def pizza():
    """ Se obtienen los datos a guardar """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print_in_console(nombre, apellidos)
    save_in_file(nombre, apellidos)
    return redirect("http://localhost/PizzaHouse/solicita_pedido.html", code=302)

def print_in_console(nombre, apellidos):
    """ Se imprime en consola """
    print(nombre)
    print(apellidos)

def save_in_file(nombre, apellidos):
    """ Guardar en el fichero """
    utils.clean_file()
    persistencia.guardar_pedido(nombre, apellidos)
