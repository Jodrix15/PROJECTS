import requests as r

def getDicc_precipitation_the50s():
    '''obtiene una API de las precipitaciones de la década de los 50 y la devuelve como un diccionario'''

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1950-01-01&end_date=1959-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_precipitation_the70s():
    '''obtiene una API de las precipitaciones de la década de los 70 y la devuelve como un diccionario'''

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_precipitation_last30Years():
    '''obtiene una API de las precipitaciones de los últimos 30 años y la devuelve como un diccionario'''

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1990-01-01&end_date=2023-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def sumPrecipitations_anual(year, dates, precpList):
    '''Esta función devuelve la suma total de las precipitaciones en un año concreto'''

    sumPrecipitation = 0

    for i in range(len(dates)):
        if year in dates[i]:
            if precpList[i] >= 0.1:
                sumPrecipitation += precpList[i]

    return sumPrecipitation

def getLista_precipitacionesAnuales(dates, precpList, years):
    '''Esta función devuelve una lista con la suma de las precipitaciones anuales de los años que se le pasa por parámetros (years)'''
    sumPre = []

    for y in years:
        sumPrecipitationYear = sumPrecipitations_anual(str(y), dates, precpList)
        sumPre.append(sumPrecipitationYear)

    return sumPre

def getPrecipitacionMedia(precpList):
    '''Esta función devuelve la media de las precipitaciones en un rango de años determinado'''

    if len(precpList) == 0:
        result = 0
    else:
        result = sum(precpList) / len(precpList)

    return result