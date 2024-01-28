import Game as g
import pokemonData as pd

def startGame():
    print("WHO'S THAT POKÉMON???\n")
    pokeName, pokeSpaces = g.getLetterSpace()
    print(pokeSpaces)

    intentos = 0
    finalizar = False

    while finalizar == False:

        g.menu()
        option = g.getOption()

        if option == 1:
            finalizar = g.correctAnswer(pokeName)
            intentos += 1
            print(f"Intento Restantes: {5 - intentos}")

        elif option == 2:
            pokeSpaces = g.writeLetter(pokeName, pokeSpaces)
            print("\n"+pokeSpaces)
            intentos += 1
            print(f"Intento Restantes: {5 - intentos}")

        elif option == 3:
            print(g.getHints(1, pokeName))

        elif option == 4:
            g.help()

        else:
            print("ERROR. OPCIÓN NO VÁLIDA")

        if intentos == 5:
            finalizar = True


startGame()