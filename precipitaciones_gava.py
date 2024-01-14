import requests as r
import json as js

def getDicc_precipitation_the70s():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_precipitation_last30Years():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1990-01-01&end_date=2023-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def sumPrecipitations_anual(fecha, dates, precpList):

    sumPrecipitation = 0

    for i in range(len(dates)):
        if fecha in dates[i]:
            if precpList[i] >= 0.1:
                sumPrecipitation += precpList[i]

    return sumPrecipitation

def getListaDecada_precipitacionesAnuales(dates, precpList, years):
    sumPre = []

    for y in years:
        sumPrecipitationYear = sumPrecipitations_anual(str(y), dates, precpList)
        sumPre.append(sumPrecipitationYear)

    return sumPre

def getPrecipitacionMedia_decada(precpList):
    return sum(precpList) / len(precpList)