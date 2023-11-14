from flask import Flask, request, redirect
import persistencia

app = Flask(__name__)
@app.route("/pizza", methods=['POST'])
def helloPOST():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(nombre)
    print(apellidos)

    file = open("pedidos.txt", "w", encoding="utf-8")
    file.write("")
    file.close()

    persistencia.guardar_pedido(nombre, apellidos)

    return redirect("http://localhost/PizzaHouse/solicita_pedido.html", code=302)