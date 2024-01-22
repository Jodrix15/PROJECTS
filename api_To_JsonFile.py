
import json as js

def getFile(msj, nameFile, dicc):
    '''Esta función recibe un mensaje (msj), el nombre de un fichero (nameFile) y un diccionario (dicc).
    Si el fichero con el nombre (nameFile) existe entonces lo carga y lo devuelve como un diccionario.
    En caso de no existe el fichero (nameFile), lo creará y devolverá el diccionario que ha escrito en el fichero.
    El formato del fichero que crea es .json'''

    try:
        print(msj)
        with open(nameFile, "r") as dicc_dataFile:
            dicc_data = js.load(dicc_dataFile)

    except FileNotFoundError:
        print("El fichero no existe. Creando fichero...")

        dicc_data = dicc

        with open(nameFile, "w") as dicc_dataFile:
            js.dump(dicc_data, dicc_dataFile, indent=3)

    return dicc_data


