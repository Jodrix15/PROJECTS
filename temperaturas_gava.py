import requests as r


def getDicc_temperature_the70s():
    '''obtiene una API de la temperartura de la década de los 70 y la devuelve como un diccionario'''

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=temperature_2m_mean&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_temperature_last30Years():
    '''obtiene una API de la temperartura de los últimos 30 años y la devuelve como un diccionario'''

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1990-01-01&end_date=2023-12-31&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getTemperaturaMedia_MaxMin_anual(year, datesList, tempList):
    '''Esta función recibe como argumento un año, un lista con todas las fechas de un diccionario determinada de temperaturas
     y un lista de temperaturas. Añade en una lista las temperaturas de tempList (lista de temperaturas Máximas/Mínimas)
     que están dentro del año (year). Devuelve la temperatura media del año (year) que se le pasa como argumento'''

    temperatura_x_dia = []

    for i in range(len(datesList)):
        if year in datesList[i]:
            temperatura_x_dia.append(tempList[i])

    return sum(temperatura_x_dia) / len(temperatura_x_dia)

def getTempMedia_anual(tempMediaMax, tempMediaMin):
    '''Esta función recibe como argumento la media de las temperaturas máximas y mmínimas de un año y devuelve
    la temperatura media anual'''

    return (tempMediaMax+tempMediaMin)/2

def getLists_tempsMediaAnuales_MaxMinMed(years, list_dates, list_tempMax, list_tempMin):
    '''Esta función recibe una lista con un rango de años, una lista de fechas, una lista de las temperaturas máximas y mínimas.
     Calcula la media anual de las diferentes temperaturas de todos los años que se le pasa por parámetro. Devuelve una lista
     con una lista de la media de las temperaturas máximas, mínimas y medias de todos los años que forman parte del rango de años
     que se le pasa por parámetro (years)'''

    list_tempMaxMed = []
    list_tempMinMed = []
    list_temMeanMed = []

    for y in years:
        tempMaxMed = getTemperaturaMedia_MaxMin_anual(str(y), list_dates, list_tempMax)
        tempMinMed = getTemperaturaMedia_MaxMin_anual(str(y), list_dates, list_tempMin)
        list_tempMaxMed.append(tempMaxMed)
        list_tempMinMed.append(tempMinMed)
        list_temMeanMed.append(getTempMedia_anual(tempMaxMed, tempMinMed))

    return [list_tempMaxMed, list_tempMinMed, list_temMeanMed]

def getTempMedia_rangoAnyos(tempMediaList):
    '''Esta función recibe como argumento una lista de temperaturas medias en un rango de años determinado y devuelve
    la temperatura media en ese rango de años'''

    return sum(tempMediaList)/len(tempMediaList)

