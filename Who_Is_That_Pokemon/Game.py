import random as rand
import pokemonData as pd

def getNumRandom():
    return rand.randint(1, 151)

def getLetterSpace():
    id = getNumRandom()
    pokeName = pd.getName(id)
    pokeNameAux = pokeName
    for chr in pokeNameAux:
        pokeNameAux = pokeNameAux.replace(chr, "_ ")

    return pokeName, pokeNameAux


def menu():
    print("1. Adivinar Pokémon\n"
          "2. Decir Letra\n"
          "3. Pista\n"
          "4. Ayuda")

def getOption():
    return int(input("Escoge una opcion: "))

def help():
    print("Cómo funciona el juego")
def correctAnswer(pokeName):

    pokemonGuess = input("Cuál es ese pokémon?: ")
    finalizar = False

    if pokemonGuess == pokeName:
        finalizar = True
        print("MUY BIEN. HAS ACERTADO!!")
    else:
        print("No has acertado el pokémon")

    return finalizar

def getLetter():
    letter = input("Escribe una letra: ").lower()
    return letter

def writeLetter(pokeName, pokeSpaces):
    letter = getLetter()
    pokeSpacesAux = pokeSpaces.replace(" ", "")
    newPokeSpaces = ""
    if letter in pokeName:
        print(f"GENIAL!! El pokémon contiene la letra {letter}")
        for chr in range(0, len(pokeName)):
            if pokeName[chr] == letter:
                newPokeSpaces += letter + " "
            elif pokeSpacesAux[chr] != "_":
                newPokeSpaces += pokeSpacesAux[chr] + " "
            else:
                newPokeSpaces += "_ "

    else:
        print(f"OH, QUE PENA!! El pokémon no tiene la letra {letter}")
        newPokeSpaces = pokeSpaces

    return newPokeSpaces

def getHints(numHint, pokeName):
    
    if numHint == 1:
        hint = pd.getId(pokeName)
    elif numHint == 2:
        hint = pd.getTypes(pokeName)
    else:
        hint = pd.getImages(pokeName)

    return hint

