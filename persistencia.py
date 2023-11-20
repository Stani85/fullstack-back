""" Escritura en un fichero """
def guardar_pedido(nombre, apellidos):
    """ se guarda el nombre y apellidos en un fichero """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
