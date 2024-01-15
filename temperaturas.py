
def temperaturaMediaAnual_maxMin(year, dates, listaTemperaturas):

    temperaturaMedia = []

    for i in range(len(dates)):
        if year in dates[i]:
            temperaturaMedia.append(listaTemperaturas[i])

    return sum(temperaturaMedia)/len(temperaturaMedia)

def listaTemperaturasMedias ():
    return ""

def temperaturaMedia_anual(tempMediaMax, temMediaMin):
    return (tempMediaMax+temMediaMin)/2



