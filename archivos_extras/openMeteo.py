import requests as r
import json as js

url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=2022-12-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"

response = r.get(url)
data = response.json()
dataTxt = js.dumps(data, indent=3)

print(dataTxt)
for k in data:
    print(k, end="; ") #imprimimos todas las key valor

print("\n",data["daily"]) #imprimimos el contenido de la key 'daily'