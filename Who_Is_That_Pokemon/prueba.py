
libros={"001": {"titulo": "MEC", "Genere": "tragedia"}}

def listG(comando):
    genere = comando
    if libros["001"]["Genere"] == genere:
        print("Hola")
    else:
        print("adios")

opcionInicial = input("> ")
opcion = opcionInicial.split("-")
listG(opcion[1:])