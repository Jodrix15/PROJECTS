from ApiManager import pokemonData as pd
from chooseOption import options as o

def getHints(numHint, pokeName, dificultad):
    hint = ""
    if dificultad != "d":
        if numHint == 1:
            hint = f"ID: {pd.getId(pokeName)}"
        elif numHint == 2:
            hint = f"Tipo(s): {pd.getTypes(pokeName)}"
        else:
            pd.getImages(pokeName)
    else:
        print("\nQue pista quieres:\n"
              "1. ID del pokémon\n"
              "2. El(los) tipos del pokemon\n")
        opcion = o.getOptionInt(["1", "2"])
        if opcion == 1:
            hint = f"ID: {pd.getId(pokeName)}"
        else:
            hint = f"Tipo(s): {pd.getTypes(pokeName)}"

    return hint