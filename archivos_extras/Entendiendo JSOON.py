import requests as r
import json as js

restUrl = "https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"

response = r.get(restUrl) #nos "conectamos" a la web que le solicitamos
resText = response.text #obtenemos el texto que le hemos solicitado. Nos devuelve un string

#usando la libreria requests
resJson = response.json() #obetnemos el texto que le hemos solicitado. Nos devuelve un diccionario
print("------FORMATO JSON CON LIBRERIA REQUESTS------")
print(type(resJson))
print(resJson)


#usando la libreria json
data = js.loads(resText) #convertimos el texto anterior en formato json si tiene un formato válido. Nos devuelve un diccionario
                        #El formato json es igual al formato de un diccionario en python
print("\n------FORMATO JSON CON LIBRERIA JSON------")
print(type(data))
print(data)

print("\n**Se observa que se obtiene el mismo resultado de una forma o de otra")

print("--------------------------------------------")
print("------IMPRIMIMOS DE FORMA BONITA EL FORMATO JSON------")
jsonString = js.dumps(resJson, indent=3) #lo imprime de forma bonita, pero devuelve un string

print(jsonString)
print(type(jsonString))

print("\n-----PEDIMOS DATOS PARA COMPROBAR QUE LO HEMOS HECHO CORRECTAMENTE-----\n")

print("Data d'elaboració de l'informe ",resJson["elaborado"])

print("Municipi ",resJson["nombre"]," a la província de ",resJson["provincia"])

print("Predicció per data ",resJson["prediccion"]["dia"][0]["@attributes"]["fecha"])

print("Predicció: temperatura màxima: ",resJson["prediccion"]["dia"][0]["temperatura"]["maxima"])

print("Predicció: temperatura mínima: ",resJson["prediccion"]["dia"][0]["temperatura"]["minima"])
