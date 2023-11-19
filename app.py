from flask import Flask, request, redirect
import persistencia

app = Flask(__name__)
@app.route("/pizza", methods=['POST'])
def pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    printInConsole(nombre, apellidos)
    saveInFile(nombre, apellidos)
   
    return redirect("http://localhost/PizzaHouse/solicita_pedido.html", code=302)

def printInConsole(nombre, apellidos):
    print(nombre)
    print(apellidos)

def saveInFile(nombre, apellidos):
    cleanFile()
    persistencia.guardar_pedido(nombre, apellidos)

def cleanFile():
    file = open("pedidos.txt", "w", encoding="utf-8")
    file.write("")
    file.close()