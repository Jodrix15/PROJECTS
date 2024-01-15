def sumaPrecipitaciones(year, dates,  listaPrecipitaciones):
    suma = 0
    for i in range(len(dates)):
        if year in dates[i]:
            suma += listaPrecipitaciones[i]

    return suma