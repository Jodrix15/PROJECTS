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


def startGame():
    o.menuWelcome()
    dificultad = o.getDifficulty()
    generacion = o.getGen()

    #seguir Jugando
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
        option = g.getOption()

        if option == 1:
            isFail, msj = g.correctAnswer(pokeName)
            if isFail == False:
                finalizar = True
                os.system("cls")
                print("¡¡¡FELICIDADES!!! HAS GANADO. Aquí tienes los datos del pokémon:\n")
                pd.getPokeInfo(pokeName.lower())
                input("PULSA ENTER PARA SALIR")

            fallos, intentos, pista = updateInfoGame(isFail, intentos, fallos)
            os.system("cls")

        elif option == 2:
            pokeSpaces, isFail, msj = g.writeLetter(pokeName, pokeSpaces)
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
            g.help()
            enterClear()

        if fallos == 6:
            print("¡¡¡HAS PERDIDO!!! El pokémon era: \n")
            finalizar = True
            pd.getPokeInfo(pokeName.lower())
            input("PULSA ENTER PARA SALIR")




startGame()