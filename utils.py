""" Utils """
def clean_file():
    """ Se vacia el fichero """
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
