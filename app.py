""" app pizza """
from flask import Flask, request, redirect, Response
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

@app.route("/checksize",methods=['POST'])
def check_aize():
    """ Comprueba disponibilidad de un tamaño de pizza. """
    size = request.form.get("size")
    if(size == "S"):
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
