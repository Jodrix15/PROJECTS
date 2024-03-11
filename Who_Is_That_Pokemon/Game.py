from ApiManager import pokemonData as pd
from chooseOption import options as o
from chooseOption import menu as m
import os
from difficulty import modosDificultad as md
from interface import interfaz as itz
from utils import Utils as u
import Pistas as p

lettersUsed = []

def getLetterSpace(numGen):
    lettersUsed.clear()
    id = o.getPokemonByGen(numGen)
    pokeName = pd.getName(id)
    pokeNameAux = pokeName
    if id == 29 or id == 32:
        pokeNameAux = "nidoran"
    for chr in pokeNameAux:
        pokeNameAux = pokeNameAux.replace(chr, "_ ")

    return pokeName.upper(), pokeNameAux


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

def writeLetter(pokeName, pokeSpaces, dificultad):
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
                if dificultad == "d":
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
            lettersUsed.append(letter)

    return newPokeSpaces, isFail, msj, volver



def updateInfoGame(isFail, intentos, vidas, numFallos):

    if isFail:
        vidas -= 1
        numFallos += 1
    intentos += 1
    pista = 0

    return vidas, intentos, pista, numFallos

def newGame(keepPlaying, dificultad, generacion):
    opcionKeepPlaying = o.getOptionChr(["s", "n"], "Quieres seguir jugando?(S/N): ")
    if opcionKeepPlaying == "n":
        keepPlaying = False
    else:
        opcionCambiarDificultad = o.getOptionChr(["s", "n"], "Quieres cambiar la dificultad?(S/N): ")
        if opcionCambiarDificultad == "s":
            dificultad = md.getSelectDificulty()
            if dificultad == "garmendia":
                dificultad = "d"
                generacion = 888
            elif dificultad == "s":
                keepPlaying = False
            else:
                opcionCambiarGen = o.getOptionChr(["s", "n"], "Quieres cambiar la generación?(S/N): ")
                if opcionCambiarGen == "s":
                    generacion = o.getGen()
                    if generacion == 6:
                        keepPlaying = False
                else:
                    if generacion == 888:
                        generacion = 1

    return keepPlaying, dificultad, generacion


def startGame():
    os.system("cls")
    keepPlaying = True
    m.menuWelcome()
    dificultad = md.getSelectDificulty()

    if dificultad != "s":
        if dificultad != "garmendia":
            generacion = o.getGen()
            os.system("cls")
        else:
            generacion = 888
            dificultad = "d"
            os.system("cls")

        if generacion != 6:
            while keepPlaying:
                intentos = 1
                finalizar = False
                pistasDisponibles = md.numPistas(dificultad)
                pista = 0
                vidas = md.numVidas(dificultad)
                numFallos = 0
                pokeName, pokeSpaces = getLetterSpace(generacion)
                pistas = []
                msj = ""
                numHint = 1

                while not finalizar:

                    itz.showGame(intentos, pistas, pokeSpaces, vidas, msj, numFallos, dificultad, pistasDisponibles)
                    option = o.getOptionInt(["1", "2", "3", "4"])

                    if option == 1:
                        isFail, msj, volver = correctAnswer(pokeName)

                        if not u.volverAtras(volver):
                            if not isFail:
                                finalizar = True
                                os.system("cls")
                                print("¡¡¡FELICIDADES, HAS GANADO!!! Aquí tienes los datos del pokémon:\n")
                                pd.getPokeInfo(pokeName.lower())
                                keepPlaying, dificultad, generacion = newGame(keepPlaying, dificultad, generacion)
                                input("PULSA ENTER")

                            vidas, intentos, pista, numFallos = updateInfoGame(isFail, intentos, vidas, numFallos)
                            os.system("cls")

                    elif option == 2:
                        pokeSpaces, isFail, msj, volver = writeLetter(pokeName, pokeSpaces, dificultad)

                        if not u.volverAtras(volver):
                            vidas, intentos, pista, numFallos = updateInfoGame(isFail, intentos, vidas, numFallos)
                            if isComplete(pokeSpaces):
                                finalizar = True
                                os.system("cls")
                                print("¡¡¡FELICIDADES, HAS GANADO!!! Aquí tienes los datos del pokémon:\n")
                                pd.getPokeInfo(pokeName.lower())
                                keepPlaying, dificultad, generacion = newGame(keepPlaying, dificultad, generacion)
                            os.system("cls")

                    elif option == 3:

                        if pistasDisponibles > 0 and pista == 0:
                            pistasDisponibles -= 1

                            if numHint != 3:
                                hint = p.getHints(numHint, pokeName.lower(), dificultad)
                                print("La pista es => "+ hint)
                                pistas.append(hint)
                            else:
                                p.getHints(numHint, pokeName.lower(), dificultad)
                            pista = 1
                            numHint += 1
                        else:
                            print("Solo una pista por turno hasta un máximo de tres")
                        u.enterClear()

                    elif option == 4:
                        finalizar = True
                        keepPlaying = False
                        u.enterClear()

                    if vidas == 0:
                        print("¡¡¡HAS PERDIDO!!! El pokémon era: \n")
                        finalizar = True
                        pd.getPokeInfo(pokeName.lower())
                        keepPlaying, dificultad, generacion = newGame(keepPlaying, dificultad, generacion)

            print("\n¡¡¡HASTA LA PRÓXIMA!!!\n")
            u.enterClear()

