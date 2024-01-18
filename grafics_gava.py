import data_gava as cg
import matplotlib.pyplot as plt
import numpy as np

def barGraph_precipitaciones_Last30Years():

    RANGO_ANYOS = 30

    data_precp = cg.data_sumPrecipitiaciones_last30Years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")
    years = data_precp[2]
    sumPre = data_precp[0]
    media = data_precp[1]

    plt.bar(years, sumPre)
    plt.subplot()
    plt.xlabel("Year")
    plt.ylabel("Suma Precp. Anual (mm)")
    plt.axhline(y=media, color="red")

    plt.show()

def pieGraph_mediaPrecp_70vs80vsLast10():
    dataList = cg.data_sumpPrecipitaciones_70vs90vsLast10()
    media_70s = dataList[0]
    media_90s = dataList[1]
    media_last10Years = dataList[2]
    total = media_70s + media_90s + media_last10Years
    porcentajes = [media_70s/total*100, media_90s/total*100, media_last10Years/total*100]
    colores = ["#2E5B88", "#B9DDF1", "#73A4CA"]

    labels = ["Los 70s", "Los 90s", "Últimos 10 años"]
    langs = [f"{porcentajes[0]:.2f}%", f"{porcentajes[1]:.2f}%", f"{porcentajes[2]:.2f}%"]
    plt.pie(dataList, labels=langs, colors = colores)
    plt.title("% de la media de precipitaciones totales en tres décadas aisladas")
    plt.legend(labels,loc='upper center', bbox_to_anchor=(1, 0.9))

    plt.show()

def graphTempMed_Last30Years():
    RANGO_ANYOS = 30
    temperatures_lists = cg.data_temperaturasMedia_last30years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")
    ancho_barra = 0.4
    indice = np.arange(1993, 2024)

    fig, ax =plt.subplots()
    ax.bar(indice+0.2, temperatures_lists[0], width = ancho_barra, label='Temperatura media máxima', align="center")
    ax.bar(indice-0.2, temperatures_lists[1],  width = ancho_barra, label='Temperatura media mínima')
    ax.plot(indice, temperatures_lists[2], color="yellow", label="Temperatura media total")

    plt.xlabel('Años', ha="center")
    plt.ylabel('Temperatura (ºC)')
    plt.legend(loc='upper center', bbox_to_anchor=(0.875, 1.16))

    plt.show()

def graph_3Anyos_TempMediaMasAlta():
    RANGO_ANYOS = 30
    temperatures_lists = cg.data_temperaturasMedia_last30years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")
    anyos = []
    temperaturas = []
    list_30years = temperatures_lists[3]
    list_tempMediaMax = temperatures_lists[2]

    for num_anyos in range(3):
        tempMax = None
        for i in range(len(list_tempMediaMax)):

            if (tempMax is None or list_tempMediaMax[i] >= tempMax) and list_30years[i] not in anyos and len(anyos)<3:
                tempMax = list_tempMediaMax[i]
                aux = i

        anyos.append(list_30years[aux])
        temperaturas.append(list_tempMediaMax[aux])

    anchoBarras = 1
    valores_x = [2, 1, 3]
    valores_y = [8, 5, 3]

    plt.bar(valores_x, valores_y, anchoBarras, color=['red', 'green', 'blue'])
    plt.xticks(valores_x, anyos)
    plt.xlabel('Categorías')
    plt.yticks([])

    plt.title("Top 3 - Años con la temperatura más alta")
    plt.show()


def graph_3Anyos_TempMasBaja():
    RANGO_ANYOS = 30
    temperatures_lists = cg.data_temperaturasMedia_last30years(RANGO_ANYOS, "Cargando diccionario de temperaturas de los últimos 30 años...")
    anyos = []
    temperaturas = []
    list_30years = temperatures_lists[3]
    list_tempMediaMin = temperatures_lists[2]

    for num_anyos in range(3):
        tempMin = None
        aux = -1
        for i in range(len(list_tempMediaMin)):

            if (tempMin is None or list_tempMediaMin[i] <= tempMin) and list_30years[i] not in anyos and len(anyos) < 3:
                tempMin = list_tempMediaMin[i]
                aux = i

        anyos.append(list_30years[aux])
        temperaturas.append(list_tempMediaMin[aux])

    valores_x = [2, 1, 3]
    valores_y = [10, 5, 2]

    plt.bar(valores_x, valores_y, color=['red', 'green', 'blue'])
    plt.xticks(valores_x, anyos)
    plt.xlabel('Categorías')
    plt.yticks([])

    plt.title("Top 3 - Años con la temperatura más baja")
    plt.show()


def plotGraph_tempEvolution_70vs90vsLast10Years():

    data = cg.data_temperaturaMedia_70vs90vsLast10()

    ejeX = ["Los 70s", "Los 90s", "Últimos 10 años"]
    ejeY = [data[0], data[1], data[2]]

    plt.plot(ejeX, ejeY)
    plt.scatter(ejeX, ejeY)
    plt.title("Evolución de la temperatura media")
    plt.show()


#barGraph_precipitaciones_Last30Years()
#graphTempMed_Last30Years()
#graph_3Anyos_TempMediaMasAlta()
#graph_3Anyos_TempMasBaja()
#pieGraph_mediaPrecp_70vs80vsLast10()
#plotGraph_tempEvolution_70vs90vsLast10Years()


