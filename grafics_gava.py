import data_gava as cg
import matplotlib.pyplot as plt
import numpy as np


def barGraph_precipitaciones_Last30Years():

    RANGO_ANYOS = 30

    data_precp = cg.data_sumPrecipitiaciones_last30Years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")
    years = data_precp[2]
    sumPre = data_precp[0]
    media = data_precp[1]
    labels = [f"media = {media:.2f} mm"]

    plt.bar(years, sumPre)
    plt.subplot()
    plt.xlabel("Años")
    plt.ylabel("Precipitaciones (mm)")
    plt.title("Suma precipitaciones anual")
    plt.axhline(y=media, color="red", linewidth=2)
    plt.legend(labels)

    plt.show()

def pieGraph_mediaPrecp_50vs70vsLast10():
    dataList = cg.data_mediaPrecipitaciones_50vs70vsLast10()
    media_70s = dataList[1]
    media_50s = dataList[0]
    media_last10Years = dataList[2]
    total = media_70s + media_50s + media_last10Years
    porcentajes = [media_50s/total*100, media_70s/total*100, media_last10Years/total*100]
    colores = ["#B9DDF1", "#73A4CA", "#2E5B88"]

    labels = ["Los 50s", "Los 70s", "Últimos 10 años"]
    langs = [f"{porcentajes[0]:.2f}%", f"{porcentajes[1]:.2f}%", f"{porcentajes[2]:.2f}%"]
    plt.pie(dataList, labels = langs, colors = colores)
    plt.title("% de la media de precipitaciones totales en tres décadas aisladas")
    plt.legend(labels,loc='upper center', bbox_to_anchor=(1.1, 0.9))

    plt.show()

def barGraphTempMed_Last30Years():
    RANGO_ANYOS = 30
    temperatures_lists = cg.data_temperaturasMedia_last30years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")[0]
    ancho_barra = 0.4
    indice = np.arange(1993, 2024)

    fig, ax =plt.subplots()
    ax.bar(indice+0.2, temperatures_lists[0], width = ancho_barra, label='Temperatura media máxima', align="center")
    ax.bar(indice-0.2, temperatures_lists[1],  width = ancho_barra, label='Temperatura media mínima')
    ax.plot(indice, temperatures_lists[2], color="red", label="Temperatura media total")

    plt.xlabel('Años', ha="center")
    plt.ylabel('Temperatura (ºC)')
    plt.legend(loc='upper center', bbox_to_anchor=(0.875, 1.16))

    plt.show()


def top3Graph_TempMediaMasAltaYBaja_last30Years():
    RANGO_ANYOS = 30
    temperatures_lists, anyos = cg.data_temperaturasMedia_last30years(RANGO_ANYOS,
                                                                      "Cargando diccionario de temperaturas de los últimos 30 años...")
    tempMedia = temperatures_lists[2]

    for i in range(len(tempMedia)):
        for j in range(i + 1, len(tempMedia)):
            if tempMedia[i] > tempMedia[j]:
                aux = tempMedia[i]
                tempMedia[i] = tempMedia[j]
                tempMedia[j] = aux

                aux = anyos[i]
                anyos[i] = anyos[j]
                anyos[j] = aux

    top3Alta = [anyos[-1], anyos[-2], anyos[-3]]
    top3Baja = [anyos[0], anyos[1], anyos[2]]

    anchoBarras = 1
    valores_x = [2, 1, 3]
    valores_y = [8, 5, 3]

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.bar(valores_x, valores_y, anchoBarras, color=['#c89a3c', '#758087', '#a05822'])

    ax1.set_xticks(valores_x, top3Alta)
    ax1.set_xlabel('Categorías')
    ax1.set_yticks([])
    ax1.set_title("Top 3 - Años con la temperatura más alta")

    ax2.bar(valores_x, valores_y, anchoBarras, color=['#c89a3c', '#758087', '#a05822'])
    ax2.set_xticks(valores_x, top3Baja)
    ax2.set_xlabel('Categorías')
    ax2.set_yticks([])
    ax2.set_title("Top 3 - Años con la temperatura más baja")

    plt.tight_layout()
    plt.show()

def plotGraph_tempEvolution_70vs90vsLast10Years():

    data= cg.data_temperaturaMedia_50vs70vsLast10()

    ejeX = ["Los 70s", "Los 90s", "Últimos 10 años"]
    ejeY = [data[0], data[1], data[2]]

    fig, ax = plt.subplots()
    ax.scatter(ejeX, ejeY, color="red")
    ax.plot(ejeX, ejeY, color="orange", linewidth = 2)

    plt.ylabel("Grados (ºC)")
    plt.xlabel("Años (Por Décadas)")
    plt.title("Evolución de la temperatura media")
    plt.show()



#barGraph_precipitaciones_Last30Years()
#barGraphTempMed_Last30Years()
#top3Graph_TempMediaMasAltaYBaja_last30Years()
#pieGraph_mediaPrecp_50vs70vsLast10()
#plotGraph_tempEvolution_70vs90vsLast10Years()


