import pokemonData as pd
import json as js

urlPokemonData = "https://pokeapi.co/api/v2/pokemon/"
urlSpecies = "https://pokeapi.co/api/v2/pokemon-species/"

specie = pd.getResponse(urlSpecies, 25)
specieURL = specie["evolution_chain"]["url"]
evoluciones = pd.doRequest(specieURL).json()

print(evoluciones.keys())
print(js.dumps(evoluciones["chain"], indent=3))






