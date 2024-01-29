import Game as g
import os
import pokemonData as pd

def interface(intentos, pokeSpaces):
    print("===============WHO'S THAT POKÉMON???===============\n")

    print(g.getAhorcado(intentos, pokeSpaces)+"\n"+
          "===================================================")

def startGame():

    intentos = 0
    finalizar = False
    pistasUsadas = 0
    pista = 0
    pokeName, pokeSpaces = g.getLetterSpace()
    pistas = []

    while finalizar == False:

        print(f"\nIntentos Restantes: {6 - intentos}")
        if len(pistas) > 0 and len(pistas)<3:
            print("Pistas => ", end="")
            for i in range(len(pistas)):
                print(f"{pistas[i]}", end="\t")
        print("\n")
        interface(intentos, pokeSpaces)
        g.menu()
        option = g.getOption()

        if option == 1:
            finalizar = g.correctAnswer(pokeName)
            intentos += 1
            pista = 0
            os.system("cls")

        elif option == 2:
            pokeSpaces = g.writeLetter(pokeName, pokeSpaces)
            intentos += 1
            pista = 0
            os.system("cls")

        elif option == 3:

            if pistasUsadas < 3 and pista == 0:
                pistasUsadas += 1
                if pistasUsadas < 3:
                    print("La pista es: "+g.getHints(pistasUsadas, pokeName.lower()))
                    pistas.append(g.getHints(pistasUsadas, pokeName.lower()))
                else:
                    g.getHints(pistasUsadas, pokeName.lower())
                pista = 1
            else:
                print("Solo una pista por turno hasta un máximo de tres")

            input("PULSA ENTER")
            os.system("cls")


        elif option == 4:
            g.help()
            input("PULSA ENTER")
            os.system("cls")

        else:
            print("ERROR. OPCIÓN NO VÁLIDA")

        if intentos == 6:
            print(pokeName)
            finalizar = True


startGame()