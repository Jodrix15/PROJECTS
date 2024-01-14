import requests as r
import json as js

def getFile(msj, nameFile, dicc):
    try:
        print(msj)
        with open(nameFile, "r") as dicc_dataFile:
            dicc_data = js.load(dicc_dataFile)

    except FileNotFoundError:
        print("El fichero no existe. Creando fichero...")

        dicc_data = dicc

        with open(nameFile, "w") as dicc_precipitationFile:
            js.dump(dicc_data, dicc_precipitationFile, indent=3)

    return dicc_data

