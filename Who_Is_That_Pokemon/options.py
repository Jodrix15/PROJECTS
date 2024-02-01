import random as rand

def menuWelcome():
    print("\n=======BIENVENIDO AL POKEHORCADO=======")
def menuGen():
    print("\nElige la generación Pokémon con la que quieras jugar\n(solo saldrán pokémons de esa generación):\n\n"+
          "1. Primera Generación\n"
          "2. Segunda Generación\n"
          "3. Tercera Generación\n"
          "4. Cuarta Generación\n"
          "5. Jugar con todos los pokémon\n")

def menuDifficulty():
    print("\nElige la dificultad:\n\n"
          "1. Fácil\n"
          "2. Normal\n"
          "3. Difícil\n"
          "4. Ayuda")


def getOptionInt(opciones):
    opcion = input("Escoge una opcion: ")
    while not opcion.isnumeric() or opcion not in(opciones):
        opcion = input(f"Debe ser un número entre 1 y {len(opciones)}\nEscoge una opcion: ")

    return int(opcion)

def getOptionChr(opciones, msj):
    opcion = input(msj).lower()
    while opcion not in(opciones):
        opcion = input(f"ERROR. Escribe 's' o 'n': ").lower()

    return opcion

def getPokemonID(numStartGen, numEndGen):
    return rand.randint(numStartGen, numEndGen)


def getGen():
    menuGen()
    opcion = getOptionInt(["1", "2", "3", "4", "5"])
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

    return pokemonID

def getDifficulty():
    menuDifficulty()
    opcion = getOptionInt(["1", "2", "3", "4"])

    if opcion == 1:
        dificultad = "f"

    elif opcion == 2:
        dificultad = "n"

    elif opcion == 3:
        dificultad = "d"


    return dificultad

