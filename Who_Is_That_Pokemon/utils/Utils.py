import os

def enterClear():
    input("PULSA ENTER")
    os.system("cls")

def volverAtras(volver):
    if volver:
        os.system("cls")
    return volver