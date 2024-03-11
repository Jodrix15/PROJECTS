import chooseOption as o
import utils as u
import chooseOption as c

def getSelectDificulty():
    terminarSeleccion = False
    dificultad = ""
    while not terminarSeleccion:
        dificultad = o.options.getDifficulty("\nEscoge la dificultad del juego: ")

        if dificultad in ["f", "n", "d", "s", "garmendia"]:
            terminarSeleccion = True
        elif dificultad == "i":
            c.menu.help()
            u.Utils.enterClear()


    return dificultad

def numVidas(difficulty):

    if difficulty == "f":
        vidas = 6
    elif difficulty == "n":
        vidas = 5
    elif difficulty == "d":
        vidas = 3

    return vidas

def numPistas(difficulty):

    if difficulty == "f":
        pistas = 3
    elif difficulty == "n":
        pistas = 2
    elif difficulty == "d":
        pistas = 1

    return pistas