def guardar_pedido(nombre, apellidos):
    file = open("pedidos.txt", "a", encoding="utf-8")
    file.write(nombre + " " + apellidos + "\n")
    file.close()