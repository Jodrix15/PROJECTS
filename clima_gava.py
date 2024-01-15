import requests as r
import json as js

def getDicc_Precipitation_the70s():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_Precipitation_last30Years():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1990-01-01&end_date=2023-12-31&daily=precipitation_sum&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_temperature_the70s():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.300526&longitude=2.0659971&start_date=1970-01-01&end_date=1979-12-31&daily=temperature_2m_mean&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getDicc_temperature_last30Years():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=1993-01-01&end_date=2023-12-31&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"
    response = r.get(url)
    return response.json()

def getFile(msj, nameFile, getDicc):
    try:
        print(msj)
        with open(nameFile, "r") as dicc_File:
            dicc = js.load(dicc_File)

    except FileNotFoundError:
        print("El fichero no existe. Creando fichero...")
        dicc = getDicc

        with open(nameFile, "w") as dicc_temperatureFile:
            js.dump(dicc, dicc_temperatureFile, indent=3)

    return dicc


def getMediaTempMin_byYear(year, dates, dicc_tempMin):

    yearDayList_tempMin = []

    for i in range(len(dates)):
        if year in dates[i]:
            yearDayList_tempMin.append(dicc_tempMin[i])

    return sum(yearDayList_tempMin) / len(yearDayList_tempMin)


def getMediaTempMax_byYear(year, dates, dicc_tempMax):

    yearDayList_tempMax = []

    for i in range(len(dates)):
        if year in dates[i]:
            yearDayList_tempMax.append(dicc_tempMax[i])

    return sum(yearDayList_tempMax) / len(yearDayList_tempMax)

def getTempMed_byYear(tempMediaMax, tempMediaMin):
    return (tempMediaMax+tempMediaMin)/2

def getMediaTempMed_byDecade(tempMediaList):
    return sum(tempMediaList)/len(tempMediaList)

def data_temperaturaMedia_last30years(rangoAnyo, msj):
    dicc_temperature = get_temperatureFile_last30years(msj)
    dates = dicc_temperature["daily"]["time"]
    dicc_tempMin = dicc_temperature["daily"]["temperature_2m_min"]
    dicc_tempMax = dicc_temperature["daily"]["temperature_2m_max"]

    if rangoAnyo == 30:
        years = [y for y in range(1993, 2024)]
        list_tempMaxMed = []
        list_tempMinMed = []
        list_temMeanMed = []

        for y in years:
            tempMaxMed = getMediaTempMax_byYear(str(y), dates, dicc_tempMax)
            tempMinMed = getMediaTempMin_byYear(str(y), dates, dicc_tempMin)
            list_tempMaxMed.append(tempMaxMed)
            list_tempMinMed.append(tempMinMed)
            list_temMeanMed.append(getTempMed_byYear(tempMaxMed, tempMinMed))


    elif rangoAnyo == 90:

        years = [y for y in range(1990, 2000)]
        list_tempMaxMed = []
        list_tempMinMed = []
        list_temMeanMed = []

        for y in years:
            tempMaxMed = getMediaTempMax_byYear(str(y), dates, dicc_tempMax)
            tempMinMed = getMediaTempMin_byYear(str(y), dates, dicc_tempMin)
            list_tempMaxMed.append(tempMaxMed)
            list_tempMinMed.append(tempMinMed)
            list_temMeanMed.append(getTempMed_byYear(tempMaxMed, tempMinMed))

    elif rangoAnyo == 10:
        years = [y for y in range(2013, 2024)]
        list_tempMaxMed = []
        list_tempMinMed = []
        list_temMeanMed = []

        for y in years:
            tempMaxMed = getMediaTempMax_byYear(str(y), dates, dicc_tempMax)
            tempMinMed = getMediaTempMin_byYear(str(y), dates, dicc_tempMin)
            list_tempMaxMed.append(tempMaxMed)
            list_tempMinMed.append(tempMinMed)
            list_temMeanMed.append(getTempMed_byYear(tempMaxMed, tempMinMed))

    else:
        print("ERROR. Algo inesperado ha ocurrido")
        list_tempMaxMed = []
        list_tempMinMed = []
        list_temMeanMed = []
        years = []


    return [list_tempMaxMed, list_tempMinMed, list_temMeanMed, years]

def data_temperaturaMedia_70vs90vsLast10():
    dicc_temperature_the90s = data_temperaturaMedia_last30years(90, "Cargando diccionario de las temperaturas de los años 90...")
    dicc_temperature_last10Years = data_temperaturaMedia_last30years(10, "Cargando diccionario de las temperaturas de los últimos 10 años...")
    dicc_temperature_the70s = get_temperatureFile_the70s("Cargando diccionario de temperaturas de los años 70...")

    listTempMedia_70s = dicc_temperature_the70s["daily"]["temperature_2m_mean"]
    listTempMedia_90s = dicc_temperature_the90s[2]
    listTempMedia_last10Years = dicc_temperature_last10Years[2]

    media_70s = getMediaTempMed_byDecade(listTempMedia_70s)
    media_90s = getMediaTempMed_byDecade(listTempMedia_90s)
    media_last10Years = getMediaTempMed_byDecade(listTempMedia_last10Years)

    return [media_70s, media_90s, media_last10Years]

def sumPrecipitations_byYear(fecha, dates, precpList):

    sumPrecipitation = 0

    for i in range(len(dates)):
        if fecha in dates[i]:
            if precpList[i] >= 0.1:
                sumPrecipitation += precpList[i]

    return sumPrecipitation

def data_sumPrecipitiaciones_last30Years(rangoAnyos, msj):

    diccPrecp = get_precipitationFile_last30Years(msj)
    dates = diccPrecp["daily"]["time"]
    precpList = diccPrecp["daily"]["precipitation_sum"]

    if rangoAnyos == 30:
        years = [y for y in range(1993, 2024)]
        sumPre = []

        for y in years:
            sumPrecipitationYear = sumPrecipitations_byYear(str(y), dates, precpList)
            sumPre.append(sumPrecipitationYear)

        media = sum(sumPre) / len(sumPre)

    elif rangoAnyos == 90:
        years = [y for y in range(1990, 2000)]
        sumPre = []

        for y in years:
            sumPrecipitationYear = sumPrecipitations_byYear(str(y), dates, precpList)
            sumPre.append(sumPrecipitationYear)

        media = sum(sumPre) / len(sumPre)

    elif rangoAnyos == 10:
        years = [y for y in range(2023, 2012, -1)]
        sumPre = []

        for y in years:
            sumPrecipitationYear = sumPrecipitations_byYear(str(y), dates, precpList)
            sumPre.append(sumPrecipitationYear)

        media = sum(sumPre) / len(sumPre)

    else:
        print("ERROR. Algo has salido mal...")
        years = []
        sumPre = []
        media = 0

    return [sumPre, media, years]

def data_sumpPrecipitaciones_70vs90vsLast10():
    ONE_DECADE = 10
    data_precp_90 = data_sumPrecipitiaciones_last30Years(90, "Cargando diccionario de temperaturas de los años 90...")
    data_precp_last10Years = data_sumPrecipitiaciones_last30Years(10, "Cargando diccionario de temperaturas de los últimos 10 años...")

    #Los 70
    dicc_sumPrecipitations_70s = get_precipitationFile_the70s("Cargando diccionario de temperaturas de los años 70...")
    sumPrecipitation_70s = sum(dicc_sumPrecipitations_70s["daily"]["precipitation_sum"])

    #Medias de las décadas
    media_sumPrecp_70s = sumPrecipitation_70s / ONE_DECADE
    media_sumPrecp_90s = data_precp_90[1]
    media_sumPrecp_last10Years = data_precp_last10Years[1]

    return [media_sumPrecp_70s, media_sumPrecp_90s, media_sumPrecp_last10Years]



