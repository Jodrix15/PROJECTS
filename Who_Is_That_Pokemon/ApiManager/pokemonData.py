import requests as r
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

urlPokemonData = "https://pokeapi.co/api/v2/pokemon/"
urlSpecies = "https://pokeapi.co/api/v2/pokemon-species/"
evolutionChain = []

def doRequest(url):
    return r.get(url)

def getResponse(url, poke):
    peticion = doRequest(url + f"{poke}")
    return peticion.json()

def getPokemonEvolutions(diccEvolucion):

    if len(diccEvolucion["evolves_to"]) != 0:
        evoluciones_dicc = diccEvolucion["evolves_to"][0]
        getPokemonEvolutions(evoluciones_dicc)
        evolutionChain.append(diccEvolucion["species"]["name"])
    else:
        evolutionChain.append(diccEvolucion["species"]["name"])

def getEvolutionChain(urlEvolutionChain):
    response = doRequest(urlEvolutionChain).json()
    getPokemonEvolutions(response["chain"])

def getName(id):
    return getResponse(urlPokemonData, id)["name"]

def getId(name):
    return getResponse(urlPokemonData, name)["id"]

def getTypes(poke):
    typesList = getResponse(urlPokemonData, poke)["types"]
    typeName = []
    for tp in typesList:
        typeName.append(tp["type"]["name"])
    return typeName

def getImages(poke):

    peticion = doRequest(getResponse(urlPokemonData, poke)["sprites"]["front_default"])
    img = Image.open(BytesIO(peticion.content))
    plt.imshow(img)
    plt.axis("off")
    return plt.show()

def getPokeInfo(poke):
    print(f"================ {getName(poke).upper()} ================\n"
          f"Identificador: {getId(poke)}\n"
          f"Altura: {getResponse(urlPokemonData, poke)['height']} dm\n"
          f"Peso: {getResponse(urlPokemonData, poke)['weight']} hg\n"
          f"Tipos: ", end=" ")

    for type in getTypes(poke):
        print(f"{type}", end="\t")

    evolutionChain.clear()
    specie = getResponse(urlSpecies, getId(poke))
    getEvolutionChain(specie["evolution_chain"]["url"])

    print(f"\nCad. Evolución: ", end="")
    for i in range(len(evolutionChain)-1, -1, -1):
        if i >= 1:
            print(evolutionChain[i], end=" => ")
        else:
            print(evolutionChain[i])

    print(f"==========================================")







