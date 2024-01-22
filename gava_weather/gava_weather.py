import requests as r
import json as js
import sys


def getAPI(fecha):
    '''obtenemos API'''
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=" + fecha + "-01&end_date=" + fecha + "-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"
    return r.get(url)

def Api2Dicc(fecha):
    '''esta función convierte lo que cogemos de la API a formato JSON (un diccionario)'''
    return getAPI(fecha).json()

def maxTemp(fecha, dates, tmpMaxList):
    '''Calcula la temperatura máxima del mes de la fecha que se ennvía como argumento'''
    temperaturaMaxima = 0

    j = 0
    for i in range(len(dates)):
        if fecha in dates[i]:
            if j == 0:
                temperaturaMaxima = tmpMaxList[i] #el primer valor de la lista se le asigna a la temperatura maxima
                j = 1
            if tmpMaxList[i] > temperaturaMaxima:
                temperaturaMaxima = tmpMaxList[i] #obtenemos la temperaturaMaxima

    return temperaturaMaxima

def minTemp(fecha, dates, tmpMinList):
    '''Calcula la temperatura mínima del mes de la fecha que se ennvía como argumento'''
    temperaturaMinima = 0

    j = 0
    for i in range(len(dates)):
        if fecha in dates[i]:
            if j == 0:
                temperaturaMinima = tmpMinList[i]
                j = 1
            if tmpMinList[i] < temperaturaMinima:
                temperaturaMinima = tmpMinList[i]

    return temperaturaMinima

def totalRainyDays(fecha, dates, rainList):
    '''esta funcion calcula el total de dias que ha llovido en la fecha que se envia por argumento'''
    rainyDays = 0

    for i in range(len(rainList)):
        if fecha in dates[i]:
            if rainList[i] >= 0.1:
                rainyDays += 1

    return rainyDays

def main():
    args = sys.argv
    fecha = args[1]

    if len(args) != 2:
        print("No valido")
    else:
        data = Api2Dicc(fecha)
        dates = data["daily"]["time"]
        tmpMaxList = data["daily"]["temperature_2m_max"]
        tmpMinList = data["daily"]["temperature_2m_min"]
        rainList = data["daily"]["rain_sum"]

        dataTxt = js.dumps(data, indent=3)
        #print(dataTxt) #descomentar para ver lo que recogemos de la web en la terminal
        print(f"Tmax = {maxTemp(fecha, dates, tmpMaxList)} ºC \tTmin = {minTemp(fecha, dates, tmpMinList)} ºC \tDies de pluja = {totalRainyDays(fecha, dates, rainList)}")

main()






