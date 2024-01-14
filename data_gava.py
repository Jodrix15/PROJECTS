import requests as r
import json as js
import api_To_JsonFile as aj
import precipitaciones_gava as pg
import temperaturas_gava as tg


def data_temperaturasMedia_last30years(rangoAnyo, msj):
    dicc_temperature = aj.getFile(msj, "dicc_temperature_last30years.json", tg.getDicc_temperature_last30Years())
    dates = dicc_temperature["daily"]["time"]
    dicc_tempMin = dicc_temperature["daily"]["temperature_2m_min"]
    dicc_tempMax = dicc_temperature["daily"]["temperature_2m_max"]

    if rangoAnyo == 30:
        years = [y for y in range(1993, 2024)]
        listas_temperaturas = tg.getLists_temps_MaxMinMed(years, dates, dicc_tempMax, dicc_tempMin)

    elif rangoAnyo == 90:
        years = [y for y in range(1990, 2000)]
        listas_temperaturas = tg.getLists_temps_MaxMinMed(years, dates, dicc_tempMax, dicc_tempMin)

    elif rangoAnyo == 10:
        years = [y for y in range(2013, 2024)]
        listas_temperaturas = tg.getLists_temps_MaxMinMed(years, dates, dicc_tempMax, dicc_tempMin)

    else:
        print("ERROR. Algo inesperado ha ocurrido")
        listas_temperaturas = []

    return listas_temperaturas

def data_temperaturaMedia_70vs90vsLast10():
    dicc_temperature_the90s = data_temperaturasMedia_last30years(90, "Cargando diccionario de las temperaturas de los años 90...")
    dicc_temperature_last10Years = data_temperaturasMedia_last30years(10, "Cargando diccionario de las temperaturas de los últimos 10 años...")
    dicc_temperature_the70s = aj.getFile("Cargando diccionario de temperaturas de los años 70...", "dicc_temperature_the70s.json", tg.getDicc_temperature_the70s())

    listTempMedia_70s = dicc_temperature_the70s["daily"]["temperature_2m_mean"]
    listTempMedia_90s = dicc_temperature_the90s[2]
    listTempMedia_last10Years = dicc_temperature_last10Years[2]

    media_70s = tg.getTempMedia_decada(listTempMedia_70s)
    media_90s = tg.getTempMedia_decada(listTempMedia_90s)
    media_last10Years = tg.getTempMedia_decada(listTempMedia_last10Years)

    return [media_70s, media_90s, media_last10Years]

def data_sumPrecipitiaciones_last30Years(rangoAnyos, msj):

    diccPrecp = aj.getFile(msj, "dicc_precipitation_last30years.json", pg.getDicc_precipitation_last30Years())
    dates = diccPrecp["daily"]["time"]
    precpList = diccPrecp["daily"]["precipitation_sum"]

    if rangoAnyos == 30:
        years = [y for y in range(1993, 2024)]
        sumPre = pg.getPrecipitationsList(dates, precpList, years)
        media = pg.getPrecipitationsMedia(sumPre)

    elif rangoAnyos == 90:
        years = [y for y in range(1990, 2000)]
        sumPre = pg.getPrecipitationsList(dates, precpList, years)
        media = pg.getPrecipitationsMedia(sumPre)

    elif rangoAnyos == 10:
        years = [y for y in range(2023, 2012, -1)]
        sumPre = pg.getPrecipitationsList(dates, precpList, years)
        media = pg.getPrecipitationsMedia(sumPre)

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
    dicc_sumPrecipitations_70s = aj.getFile("Cargando diccionario de temperaturas de los años 70...", "dicc_precipitation_the70s.json", pg.getDicc_precipitation_the70s())
    sumPrecipitation_70s = sum(dicc_sumPrecipitations_70s["daily"]["precipitation_sum"])

    #Medias de las décadas
    media_sumPrecp_70s = sumPrecipitation_70s / ONE_DECADE
    media_sumPrecp_90s = data_precp_90[1]
    media_sumPrecp_last10Years = data_precp_last10Years[1]

    return [media_sumPrecp_70s, media_sumPrecp_90s, media_sumPrecp_last10Years]


