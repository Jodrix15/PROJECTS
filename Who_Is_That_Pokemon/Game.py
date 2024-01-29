import random as rand
import pokemonData as pd

def getNumRandom():
    return rand.randint(1, 151)

def getAhorcado(intento,pokeSpaces):
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
    return ahorcado[intento]

def getLetterSpace():
    id = getNumRandom()
    pokeName = pd.getName(id)
    pokeNameAux = pokeName
    for chr in pokeNameAux:
        pokeNameAux = pokeNameAux.replace(chr, "_ ")

    return pokeName.upper(), pokeNameAux


def menu():
    print("\n1. Adivinar Pokémon\t\t"
          "2. Decir Letra\t\t"
          "3. Pista\t\t"
          "4. Ayuda")

def getOption():
    opcion = int(input("Escoge una opcion: "))
    while opcion not in (1, 2, 3, 4):
        opcion = int(input("Escoge una opcion: "))

    return opcion

def help():
    print("Cómo funciona el juego")
def correctAnswer(pokeName):

    pokemonGuess = input("Cuál es ese pokémon?: ").upper()
    finalizar = False

    if pokemonGuess == pokeName:
        finalizar = True
        print("MUY BIEN. HAS ACERTADO!!")
    else:
        print("No has acertado el pokémon")

    return finalizar

def getLetter():
    validsLetter = "abcdefghijklmnopqrstuvwxyz"
    letter = input("Escribe una letra: ").lower()
    while letter not in validsLetter or len(letter) != 1:
        letter = input("Escribe una letra: ").lower()

    return letter

def writeLetter(pokeName, pokeSpaces):
    letter = getLetter().upper()
    pokeSpacesAux = pokeSpaces.replace(" ", "")
    newPokeSpaces = ""
    if letter in pokeName:
        print(f"GENIAL!! El pokémon contiene la letra '{letter}'")
        for chr in range(0, len(pokeName)):
            if pokeName[chr] == letter:
                newPokeSpaces += letter + " "
            elif pokeSpacesAux[chr] != "_":
                newPokeSpaces += pokeSpacesAux[chr] + " "
            else:
                newPokeSpaces += "_ "

    else:
        print(f"OH, QUE PENA!! El pokémon no tiene la letra '{letter}'")
        newPokeSpaces = pokeSpaces

    return newPokeSpaces

def getHints(numHint, pokeName):
    
    if numHint == 1:
        hint = f"ID: {pd.getId(pokeName)}"
    elif numHint == 2:
        hint = f"Tipo(s): {pd.getTypes(pokeName)}"
    else:
        hint = pd.getImages(pokeName)

    return hint

