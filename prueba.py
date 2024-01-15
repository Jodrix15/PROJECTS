import clima_gava as cg
import json as js

def getFile(msj, nameFile, getDicc):
    try:
        print(msj)
        with open(nameFile, "r") as dicc_File:
            dicc = js.load(dicc_File)

    except FileNotFoundError:
        print("El fichero no existe. Creando fichero...")
        dicc = getDicc

        with open(nameFile, "w") as dicc_temperatureFile:
            js.dump(dicc, dicc_temperatureFile, indent=3)

    return dicc

