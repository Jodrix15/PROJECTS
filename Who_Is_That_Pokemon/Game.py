import random as rand
import pokemonData as pd
import options as o

lettersUsed = []

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
    lettersUsed.clear()
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
          "4. Salir\n")

def help():
    print("Cómo funciona el juego")

def isComplete(pokeName):
    complete = False
    if "_" not in pokeName:
        complete = True

    return complete



def correctAnswer(pokeName):

    pokemonGuess = input("Cuál es ese pokémon? ('BACK' para volver atrás): ").upper()
    isFail = True
    volver = False
    msj = ""

    if pokemonGuess == "BACK":
        volver = True
    else:
        if pokemonGuess == pokeName:
            isFail = False
            msj = "MUY BIEN. HAS ACERTADO!!"
        else:
            msj = "No has acertado el pokémon"

    return isFail, msj, volver

def getLetter():

    validsLetter = "abcdefghijklmnopqrstuvwxyz"
    letter = input("Escribe una letra ('BACK' para volver atrás): ").lower()

    if letter == "back":
        letter = "back"

    else:
        while letter not in validsLetter or len(letter) != 1:
            letter = input("Escribe una letra('BACK' para volver atrás): ").lower()

    return letter

def writeLetter(pokeName, pokeSpaces):
    isFail = False
    volver = False
    letter = getLetter().upper()
    if letter == "BACK":
        newPokeSpaces = pokeSpaces
        volver = True
        msj = ""
    else:
        pokeSpacesAux = pokeSpaces.replace(" ", "")
        newPokeSpaces = ""
        if letter in pokeName:
            if letter in lettersUsed:
                msj = f"¡¡¡OH VAYA!!! Parece que ya habías dicho esa letra"
                newPokeSpaces = pokeSpaces
                isFail = True
            else:
                msj = f"¡¡¡GENIAL!! El pokémon contiene la letra '{letter}'"
                for chr in range(0, len(pokeName)):
                    if pokeName[chr] == letter:
                        newPokeSpaces += letter + " "
                    elif pokeSpacesAux[chr] != "_":
                        newPokeSpaces += pokeSpacesAux[chr] + " "
                    else:
                        newPokeSpaces += "_ "
                lettersUsed.append(letter)


        else:
            msj = f"OH, QUE PENA!! El pokémon no tiene la letra '{letter}'"
            newPokeSpaces = pokeSpaces
            isFail = True

    return newPokeSpaces, isFail, msj, volver

def getHints(numHint, pokeName):
    
    if numHint == 1:
        hint = f"ID: {pd.getId(pokeName)}"
    elif numHint == 2:
        hint = f"Tipo(s): {pd.getTypes(pokeName)}"
    else:
        hint = pd.getImages(pokeName)

    return hint

