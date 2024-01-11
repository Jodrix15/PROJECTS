import requests as r
import json as js
import sys
from datetime import date as d


def maxTemp(fecha):
    temperaturaMaxima = 0
    dates = data["daily"]["time"]
    tmpMaxList = data["daily"]["temperature_2m_max"]
    j = 0
    for i in range(len(dates)):
        if fecha in dates[i]:
            if j == 0:
                temperaturaMaxima = tmpMaxList[i]
                j = 1
            if tmpMaxList[i] > temperaturaMaxima:
                temperaturaMaxima = tmpMaxList[i]

    return temperaturaMaxima


def minTemp(fecha):
    temperaturaMinima = 0
    dates = data["daily"]["time"]
    tmpMinList = data["daily"]["temperature_2m_min"]
    j = 0
    for i in range(len(dates)):
        if fecha in dates[i]:
            if j == 0:
                temperaturaMinima = tmpMinList[i]
                j = 1

            if tmpMinList[i] < temperaturaMinima:
                temperaturaMinima = tmpMinList[i]

    return temperaturaMinima


def totalRainyDays(fecha):
    rainyDays = 0
    dayList = data["daily"]["time"]
    rainList = data["daily"]["rain_sum"]

    for i in range(len(dayList)):
        if fecha in dayList[i]:
            if rainList[i] > 0.0:
                rainyDays += 1

    return rainyDays


def validarFecha(fecha):
    f = fecha.split("-")
    anyo = f[0]
    mes = f[1]
    date = d(int(anyo), int(mes), 1)
    ultimateDate = "0"

    if date <= d.today():
        ultimateDate = d.strftime(date, "%Y-%m-%d")

    return ultimateDate


fecha = "2022-1"
fechaYMD = validarFecha(fecha)

if fechaYMD == "0":
    print("Fecha no valida")
else:

    fechaYMD2 = fechaYMD.split("-")
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.002&start_date=" + fechaYMD + "&end_date=" + fechaYMD2[0]+'-'+fechaYMD2[1] + "-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"

    response = r.get(url)
    data = response.json()
    '''data = {
        "daily": {

            "time": ["2000-12-13", "2000-12-05",
                    "2020-11-13", "2020-11-05",
                    "2023-01-13", "2023-01-05"],

            "temperature_2m_max": [27.6, 30,
                                   14, 19,
                                   23, 26],

            "temperature_2m_min": [2, 5,
                                   -1, 8,
                                   3, 6],

            "rain_sum": [0.0, 0.0,
                         0.1, 13,
                         0.0, 1]
        }

    }'''
    dataTxt = js.dumps(data, indent=3)
    print(dataTxt)
    print(
        f"Tmax = {maxTemp(fechaYMD2[0]+'-'+fechaYMD2[1])} ºC \tTmin = {minTemp(fechaYMD2[0]+'-'+fechaYMD2[1])} ºC \tDies de pluja = {totalRainyDays(fechaYMD2[0]+'-'+fechaYMD2[1])}")

'''Cómo podemos asegurarnos de que lo estamos haciendo bien?'''
'''para asegurarnos que lo estamos haciendo bien podemos hacer nosotros  mismo un diccionario más corto con datos conflictivos'''

