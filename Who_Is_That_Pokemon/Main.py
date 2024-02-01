import Game as g
import os
import pokemonData as pd
import options as o

def interface(numFallo, pokeSpaces):
    print("===============WHO'S THAT POKÉMON???===============\n")

    print(g.getAhorcado(numFallo, pokeSpaces)+"\n"+
          "===================================================")

def showGame(intentos, pistas, pokeSpaces, fallos, msj):
    print("\n"+msj)
    print(f"\nTurno: {intentos}\t Vidas Restantes: {6-fallos}")
    if len(pistas) > 0 and len(pistas) < 3:
        print("Pistas => ", end="")
        for i in range(len(pistas)):
            print(f"{pistas[i]}", end="\t")
    print("\n")
    interface(fallos, pokeSpaces)
    g.menu()

def enterClear():
    input("PULSA ENTER")
    os.system("cls")

def updateInfoGame(isFail, intentos, fallos):

    if isFail:
        fallos += 1
    intentos += 1
    pista = 0

    return fallos, intentos, pista

def newGame(keepPlaying, dificultad, generacion):
    opcionKeepPlaying = o.getOptionChr(["s", "n"], "Quieres seguir jugando?(S/N): ")
    if opcionKeepPlaying == "n":
        keepPlaying = False
    else:
        opcionCambiarDificultad = o.getOptionChr(["s", "n"], "Quieres cambiar la dificultad?(S/N): ")
        if opcionCambiarDificultad == "s":
            dificultad = o.getDifficulty()

        opcionCambiarGen = o.getOptionChr(["s", "n"], "Quieres cambiar la generación?(S/N): ")
        if opcionCambiarGen == "s":
            generacion = o.getGen()

    return keepPlaying, dificultad, generacion

def volverAtras(volver):
    if volver:
        os.system("cls")
    return volver



def startGame():
    o.menuWelcome()
    dificultad = o.getDifficulty()
    generacion = o.getGen()
    keepPlaying = True

    while keepPlaying:
        intentos = 1
        finalizar = False
        pistasUsadas = 0
        pista = 0
        fallos = 0
        pokeName, pokeSpaces = g.getLetterSpace(generacion)
        pistas = []
        msj = ""

        while not finalizar:

            showGame(intentos, pistas, pokeSpaces, fallos, msj)
            option = o.getOptionInt(["1", "2", "3", "4"])


            if option == 1:
                isFail, msj, volver = g.correctAnswer(pokeName)

                if not volverAtras(volver):
                    if not isFail:
                        finalizar = True
                        os.system("cls")
                        print("¡¡¡FELICIDADES, HAS GANADO!!! Aquí tienes los datos del pokémon:\n")
                        pd.getPokeInfo(pokeName.lower())
                        keepPlaying, dificultad, generacion = newGame(keepPlaying, dificultad, generacion)
                        input("PULSA ENTER")

                    fallos, intentos, pista = updateInfoGame(isFail, intentos, fallos)
                    os.system("cls")

            elif option == 2:
                pokeSpaces, isFail, msj, volver = g.writeLetter(pokeName, pokeSpaces)

                if not volverAtras(volver):
                    fallos, intentos, pista = updateInfoGame(isFail, intentos, fallos)
                    os.system("cls")

            elif option == 3:

                if pistasUsadas < 3 and pista == 0:
                    pistasUsadas += 1
                    if pistasUsadas < 3:
                        print("La pista es => "+g.getHints(pistasUsadas, pokeName.lower()))
                        pistas.append(g.getHints(pistasUsadas, pokeName.lower()))
                    else:
                        g.getHints(pistasUsadas, pokeName.lower())
                    pista = 1
                else:
                    print("Solo una pista por turno hasta un máximo de tres")
                enterClear()

            elif option == 4:
                finalizar = True
                keepPlaying = False
                print("¡¡¡HASTA LA PRÓXIMA!!!")
                enterClear()

            if fallos == 6:
                print("¡¡¡HAS PERDIDO!!! El pokémon era: \n")
                finalizar = True
                pd.getPokeInfo(pokeName.lower())
                keepPlaying, dificultad, generacion = newGame(keepPlaying, dificultad, generacion)
                input("PULSA ENTER")


startGame()