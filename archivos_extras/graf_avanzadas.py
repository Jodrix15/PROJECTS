import requests

import json

import matplotlib.pyplot as plt

# Demanem dades de temperatura màxima, mínima i precipitacions del mes de desembre de 2022

api_url="https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date=2022-12-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"

response=requests.get(api_url)

dades=json.loads(response.text)

tempMax=dades["daily"]["temperature_2m_max"]

tempMin=dades["daily"]["temperature_2m_min"]

pluja=dades["daily"]["precipitation_sum"]

fig,ax=plt.subplots()

ax.plot(dades["daily"]["time"],tempMax)

ax.plot(dades["daily"]["time"],tempMin)

ax.bar(dades["daily"]["time"],pluja)

plt.xticks(rotation=45, ha='right')

plt.show()

