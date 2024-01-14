import requests as r
import json as js
import sys

restUrl = "https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"
htmlUrl = "https://www.eltiempo.es/gava.html"

responseHTML = r.get(htmlUrl) #conectamos con la página
print(responseHTML.text) #-> podemos ver el código fuente (código HTML) de la página

responseREST = r.get(restUrl) #conectamos con la pagina

print(responseREST.text) #nos imprime los datos que le hemos pedido
print(type(responseREST.text)) #responseREST.text nos devuelve un string

print(responseREST.url) #nos imprime la url de la pagina

print(responseREST.json()) #me devuelve el texto en formato json (un diccinario) si el formato es válido
print(type(responseREST.json()))#comprobamos que, efectivamente, responseREST.json() me devuelve un diccionario


