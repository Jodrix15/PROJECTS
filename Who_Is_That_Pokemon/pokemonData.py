import requests as r
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

def doRequest(url):
    return r.get(url)

def getPokemonData(poke):
    peticion = doRequest(f"https://pokeapi.co/api/v2/pokemon/{poke}")
    return peticion.json()

def getEvolutionChain(id):
    peticion = doRequest(f"https://pokeapi.co/api/v2/evolution-chain/{id}")

    return peticion.json()

def getName(id):
    return getPokemonData(id)["name"]

def getId(name):
    return getPokemonData(name)["id"]

def getTypes(poke):
    typesList = getPokemonData(poke)["types"]
    typeName = []
    for tp in typesList:
        typeName.append(tp["type"]["name"])

    return typeName


def getImages(poke):

    peticion = doRequest(getPokemonData(poke)["sprites"]["front_default"])
    img = Image.open(BytesIO(peticion.content))
    plt.imshow(img)
    plt.axis("off")
    return plt.show()

def getPokeInfo(poke):
    print(f"============== {getName(poke).upper()} ==============\n"
          f"Identificador: {getId(poke)}\n"
          f"Altura: {getPokemonData(poke)['height']} dm\n"
          f"Peso: {getPokemonData(poke)['weight']} hg\n"
          f"Tipos: ", end=" ")

    for type in getTypes(poke):
        print(f"{type}", end="\t")

    print(f"\nCadena de evolución: \n"
          f"======================================")

