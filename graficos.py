import clima_gava as cg
import temperaturas as t
import matplotlib.pyplot as plt
import numpy as np
import precipitaciones as p

def barGraph_temperatures_last30Years():
    dicc = cg.getFile("cargando..", "temperataras_last30years.json", cg.getDicc_temperature_last30Years())

    lista_temperaturasMaximas = dicc["daily"]["temperature_2m_max"]
    lista_temperaturasMinimas = dicc["daily"]["temperature_2m_min"]
    dates = dicc["daily"]["time"]
    listaTempMax = []
    listaTempMin = []
    listaTempMedia = []


    years = [y for y in range(1993, 2024)]
    for y in years:
        mediaTempMax = t.temperaturaMediaAnual_maxMin(str(y), dates, lista_temperaturasMaximas)
        listaTempMax.append(mediaTempMax)
        mediaTempMin = t.temperaturaMediaAnual_maxMin(str(y), dates, lista_temperaturasMinimas)
        listaTempMin.append(mediaTempMin)
        mediaTempMedia = t.temperaturaMedia_anual(mediaTempMax, mediaTempMin)
        listaTempMedia.append(mediaTempMedia)

    indice = np.arange(1993, 2024)

    fig,ax = plt.subplots()
    ax.bar(indice, listaTempMax)
    ax.bar(indice, listaTempMin)
    ax.plot(indice, listaTempMedia, color="red")

    plt.show()

def barPrecipitaciones_last30Years():
    dicc = cg.getFile("cargando..", "precipitaciones_last30years.json", cg.getDicc_Precipitation_last30Years())
    listaPrecipitaciones = dicc["daily"]["precipitation_sum"]
    dates = dicc["daily"]["time"]
    years = [y for y in range(1993, 2024)]
    lluvias = []
    for i in years:
        lluvias.append(p.sumaPrecipitaciones(str(i), dates, listaPrecipitaciones))
    mediaLluvias = sum(lluvias)/len(lluvias)
    indice = np.arange(1993, 2024)

    fig, ax = plt.subplots()
    ax.bar(indice, lluvias)
    ax.axhline(mediaLluvias, color="red")
    plt.show()

barPrecipitaciones_last30Years()






