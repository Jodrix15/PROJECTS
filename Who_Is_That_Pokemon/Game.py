import random as rand
import pokemonData as pd
import options as o

def getNumRandom():
    return rand.randint(151, 251)

def getAhorcado(numFallo, pokeSpaces):
    ahorcado = [
        "+-------+\n"
        "|       |\n"
        "|\n"
        "|                         "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|                         "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /                  "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|                 "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|      /\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|      / \\\n"
        "|\n"
        "============="
    ]
    return ahorcado[numFallo]

def getLetterSpace(numGen):
    id = o.getPokemonByGen(numGen)
    pokeName = pd.getName(id)
    pokeNameAux = pokeName
    for chr in pokeNameAux:
        pokeNameAux = pokeNameAux.replace(chr, "_ ")

    return pokeName.upper(), pokeNameAux


def menu():
    print("\n1. Adivinar Pokémon\t\t"
          "2. Decir Letra\n"
          "3. Pista\t\t\t"
          "4. Ayuda\n")

def getOption():
    opcion = input("Escoge una opcion: ")
    while not opcion.isnumeric() or opcion not in("1", "2", "3", "4"):
        opcion = input("Debe ser un número entre 1 y 4\nEscoge una opcion: ")

    return int(opcion)

def help():
    print("Cómo funciona el juego")
def correctAnswer(pokeName):

    pokemonGuess = input("Cuál es ese pokémon?: ").upper()
    isFail = True

    if pokemonGuess == pokeName:
        isFail = False
        msj = "MUY BIEN. HAS ACERTADO!!"
    else:
        msj = "No has acertado el pokémon"

    return isFail, msj

def getLetter():
    validsLetter = "abcdefghijklmnopqrstuvwxyz"
    letter = input("Escribe una letra: ").lower()
    while letter not in validsLetter or len(letter) != 1:
        letter = input("Escribe una letra: ").lower()

    return letter

def writeLetter(pokeName, pokeSpaces):
    isFail = False
    letter = getLetter().upper()
    pokeSpacesAux = pokeSpaces.replace(" ", "")
    newPokeSpaces = ""
    if letter in pokeName:
        msj = f"GENIAL!! El pokémon contiene la letra '{letter}'"
        for chr in range(0, len(pokeName)):
            if pokeName[chr] == letter:
                newPokeSpaces += letter + " "
            elif pokeSpacesAux[chr] != "_":
                newPokeSpaces += pokeSpacesAux[chr] + " "
            else:
                newPokeSpaces += "_ "


    else:
        msj = f"OH, QUE PENA!! El pokémon no tiene la letra '{letter}'"
        newPokeSpaces = pokeSpaces
        isFail = True

    return newPokeSpaces, isFail, msj

def getHints(numHint, pokeName):
    
    if numHint == 1:
        hint = f"ID: {pd.getId(pokeName)}"
    elif numHint == 2:
        hint = f"Tipo(s): {pd.getTypes(pokeName)}"
    else:
        hint = pd.getImages(pokeName)

    return hint

