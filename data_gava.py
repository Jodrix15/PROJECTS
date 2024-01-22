
import api_To_JsonFile as aj
import precipitaciones_gava as pg
import temperaturas_gava as tg



def data_temperaturasMedia_last30years(rangoAnyo, msj):
    '''Esta función nos devuelve una lista con los datos las listas de las diferentes temperaturas medias en un rango de años
     determinado que recibe como argumento'''

    dicc_temperature = aj.getFile(msj, "dicc_temperature_last30years.json", tg.getDicc_temperature_last30Years())
    list_dates = dicc_temperature["daily"]["time"]
    list_tempMin = dicc_temperature["daily"]["temperature_2m_min"]
    list_tempMax = dicc_temperature["daily"]["temperature_2m_max"]


    if rangoAnyo == 30: #últimos 30 años
        years = [y for y in range(1993, 2024)]
        listas_temperaturas = tg.getLists_tempsMediaAnuales_MaxMinMed(years, list_dates, list_tempMax, list_tempMin)

    elif rangoAnyo == 90: #década de los 90
        years = [y for y in range(1990, 2000)]
        listas_temperaturas = tg.getLists_tempsMediaAnuales_MaxMinMed(years, list_dates, list_tempMax, list_tempMin)

    elif rangoAnyo == 10: #últimos 10 años
        years = [y for y in range(2013, 2024)]
        listas_temperaturas = tg.getLists_tempsMediaAnuales_MaxMinMed(years, list_dates, list_tempMax, list_tempMin)

    else:
        print("ERROR. Algo inesperado ha ocurrido")
        listas_temperaturas = []
        years = []

    return listas_temperaturas, years

def data_temperaturaMedia_50vs70vsLast10():
    '''Esta función devuelve una lista con los datos de la media de las temperaturas en tres décadas aisladas'''

    dicc_temperature_the90s = data_temperaturasMedia_last30years(90, "Cargando diccionario de las temperaturas de los años 90...")
    dicc_temperature_last10Years = data_temperaturasMedia_last30years(10, "Cargando diccionario de las temperaturas de los últimos 10 años...")
    dicc_temperature_the70s = aj.getFile("Cargando diccionario de temperaturas de los años 70...", "dicc_temperature_the70s.json", tg.getDicc_temperature_the70s())

    listTempMedia_70s = dicc_temperature_the70s["daily"]["temperature_2m_mean"]
    listTempMedia_90s = dicc_temperature_the90s[0][2]
    listTempMedia_last10Years = dicc_temperature_last10Years[0][2]

    media_70s = tg.getTempMedia_rangoAnyos(listTempMedia_70s)
    media_90s = tg.getTempMedia_rangoAnyos(listTempMedia_90s)
    media_last10Years = tg.getTempMedia_rangoAnyos(listTempMedia_last10Years)

    return [media_70s, media_90s, media_last10Years]

def data_sumPrecipitiaciones_last30Years(rangoAnyos, msj):
    '''Esta función nos devuelve una lista que contiene los siguientes datos un lista con la suma de precipitaciones anuales
    en el rango de años que se obtiene por argumento, la media de la misma lista, y el intervalo de años
    que se ha estudiado'''

    diccPrecp = aj.getFile(msj, "dicc_precipitation_last30years.json", pg.getDicc_precipitation_last30Years())
    dates = diccPrecp["daily"]["time"]
    precpList = diccPrecp["daily"]["precipitation_sum"]

    if rangoAnyos == 30: #últimos 30 años
        years = [y for y in range(1993, 2024)]
        sumPre = pg.getLista_precipitacionesAnuales(dates, precpList, years)
        media = pg.getPrecipitacionMedia(sumPre)

    elif rangoAnyos == 10: #últimos 10 años
        years = [y for y in range(2013, 2024)]
        sumPre = pg.getLista_precipitacionesAnuales(dates, precpList, years)
        media = pg.getPrecipitacionMedia(sumPre)

    else:
        print("ERROR. Algo has salido mal...")
        years = []
        sumPre = []
        media = 0

    return [sumPre, media, years]

def data_mediaPrecipitaciones_50vs70vsLast10():
    '''Esta función devuelve una lista con los datos de la media de las precipitaciones en tres
    décadas aisladas'''

    #Ultimos 10 años
    data_precp_last10Years = data_sumPrecipitiaciones_last30Years(10, "Cargando diccionario de precipitaciones de los últimos 10 años...")

    #Los 70
    dicc_sumPrecipitations_70s = aj.getFile("Cargando diccionario de precipitaciones de los años 70...", "dicc_precipitation_the70s.json", pg.getDicc_precipitation_the70s())
    years = [y for y in range(1970, 1979)]
    sumPre = pg.getLista_precipitacionesAnuales(dicc_sumPrecipitations_70s["daily"]["time"],
                                                dicc_sumPrecipitations_70s["daily"]["precipitation_sum"],
                                                years)

    #Los 50
    dicc_sumPrecipitations_50s =aj.getFile("Cargando diccionario de precipitaciones de los años 50", "dicc_precipitation_the50s.json", pg.getDicc_precipitation_the50s())
    years50 = [y for y in range(1950, 1959)]
    sumPre50 = pg.getLista_precipitacionesAnuales(dicc_sumPrecipitations_50s["daily"]["time"],
                                                dicc_sumPrecipitations_50s["daily"]["precipitation_sum"],
                                                  years50)


    #Medias de las décadas
    media_sumPrecp_50s = pg.getPrecipitacionMedia(sumPre50)
    media_sumPrecp_70s = pg.getPrecipitacionMedia(sumPre)
    media_sumPrecp_last10Years = data_precp_last10Years[1]

    return [media_sumPrecp_50s, media_sumPrecp_70s, media_sumPrecp_last10Years]


def data_temperaturaMedia_Estaciones_70vs90vsLast10():
    '''Esta función recoge los datos de la temperatura media en las décadas de los 70, 90 y los últimos 10 años'''
    # Carga de datos

    dicc_temperature = aj.getFile("Cargando diccionario ultimos 30 años...", "dicc_temperatureMean_last30years.json",
                                  tg.getDicc_temperature_media_last30years())

    dicc_temperature_the70s = aj.getFile("Cargando diccionario de temperaturas de los años 70...",
                                         "dicc_temperature_the70s.json", tg.getDicc_temperature_the70s())

    # Listas de datos
    listTempMedia_70s = dicc_temperature_the70s["daily"]
    listTempMedia_Last30s = dicc_temperature["daily"]

    estaciones = ["Invierno", "Primavera", "Verano", "Otoño"]

    medias_70s = {}
    for estacion in estaciones:
        medias_70s[estacion] = tg.getTempMedia_porEstacion(1970, estacion, listTempMedia_70s)
    # print(medias_70s)

    medias_ultimos_30 = {}

    anyos = [1990, 2000, 2010]  # Años de las últimas 3 décadas
    for anyo in anyos:
        medias_anyo = {}
        for estacion in estaciones:
            medias_anyo[estacion] = tg.getTempMedia_porEstacion(anyo, estacion, listTempMedia_Last30s)
        medias_ultimos_30[anyo] = medias_anyo

    return medias_70s, medias_ultimos_30

def data_temperaturaMedia_enNavidad():
    '''Esta función devuelve una lista de las temperaturas medias en el día de navidad'''
    dicc_temperature = aj.getFile("Cargando diccionario de los últimos 30 años", "dicc_temperature_last30Years.json", tg.getDicc_temperature_last30Years())
    list_dates = dicc_temperature["daily"]["time"]
    list_tempMin = dicc_temperature["daily"]["temperature_2m_min"]
    list_tempMax = dicc_temperature["daily"]["temperature_2m_max"]

    listaMedia_navidad = []

    for i in range(len(list_dates)):
        if "12-25" in list_dates[i]:
            listaMedia_navidad.append((list_tempMax[i]+list_tempMin[i])/2)

    return listaMedia_navidad

