import random as rand
from chooseOption import menu as m
from utils import Utils as u


def getOptionInt(opciones):
    opcion = input("Escoge una opcion: ")
    if opcion != "garmendia":
        while not opcion.isnumeric() or opcion not in(opciones):
            opcion = input(f"Debe ser un número entre 1 y {len(opciones)}\nEscoge una opcion: ")
        opcion = int(opcion)

    return opcion

def getOptionChr(opciones, msj):
    opcion = input(msj).lower()
    while opcion not in(opciones):
        opcion = input(f"ERROR. Escribe 's' o 'n': ").lower()

    return opcion

def getPokemonID(numStartGen, numEndGen):
    return rand.randint(numStartGen, numEndGen)

def getPokemonIDGarmendia(list):
    return rand.choice(list)

def getGen():
    m.menuGen()
    opcion = getOptionInt(["1", "2", "3", "4", "5", "6"])
    return opcion

def getPokemonByGen(numGen):

    if numGen == 1:
       pokemonID = getPokemonID(1, 151)

    elif numGen == 2:
        pokemonID = getPokemonID(152, 251)

    elif numGen == 3:
        pokemonID = getPokemonID(252, 386)

    elif numGen == 4:
        pokemonID = getPokemonID(387, 493)

    elif numGen == 5:
        pokemonID = getPokemonID(1, 493)
    else:
        m.menuOculto()
        pokemonID = getPokemonIDGarmendia([389, 424, 405, 475, 468, 134])
        u.enterClear()

    return pokemonID

def getDifficulty(msj):
    print(msj)
    m.menuDifficulty()
    opcion = getOptionInt(["1", "2", "3", "4", "5"])

    if opcion == 1:
        dificultad = "f"

    elif opcion == 2:
        dificultad = "n"

    elif opcion == 3:
        dificultad = "d"
    elif opcion == 4:
        dificultad = "i"
    elif opcion == 5:
        dificultad = "s"
    else:
        dificultad = "garmendia"

    return dificultad

