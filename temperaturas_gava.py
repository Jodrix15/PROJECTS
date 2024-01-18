import requests as r


def getDicc_temperature_the70s():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=temperature_2m_mean&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_temperature_last30Years():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1990-01-01&end_date=2023-12-31&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getTemperaturaMedia_MaxMin_anual(year, dates, dicc):

    temperatura_x_dia = []

    for i in range(len(dates)):
        if year in dates[i]:
            temperatura_x_dia.append(dicc[i])

    return sum(temperatura_x_dia) / len(temperatura_x_dia)

def getTempMedia_anual(tempMediaMax, tempMediaMin):
    return (tempMediaMax+tempMediaMin)/2

def getListsDecada_tempsMediaAnuales_MaxMinMed(years, dates, dicc_tempMax, dicc_tempMin):
    list_tempMaxMed = []
    list_tempMinMed = []
    list_temMeanMed = []

    for y in years:
        tempMaxMed = getTemperaturaMedia_MaxMin_anual(str(y), dates, dicc_tempMax)
        tempMinMed = getTemperaturaMedia_MaxMin_anual(str(y), dates, dicc_tempMin)
        list_tempMaxMed.append(tempMaxMed)
        list_tempMinMed.append(tempMinMed)
        list_temMeanMed.append(getTempMedia_anual(tempMaxMed, tempMinMed))

    return [list_tempMaxMed, list_tempMinMed, list_temMeanMed]

def getTempMedia_decada(tempMediaList):
    return sum(tempMediaList)/len(tempMediaList)