import matplotlib.pyplot as plt
import data_gava as cg

dicc = {
    "daily": {
        "time": [
            "1",
            "1",
            "1",
            "1",
            "2",
            "2",
            "3",
            "4",
            "5",
            "6",
            "6",
            "6",
            "7",
            "8",
            "9",
            "10"
        ],
        "precipitation_sum": [
            3,
            5,
            6,
            7,
            8,
            2,
            3,
            5,
            1,
            3,
            5,
            6,
            2,
            3,
            4,
            2
        ]
    }
}
def precipitacionesLast30Years():
    years = []
    sumPre = []
    sum = 0
    for year in range(1, 11):
        years.append(year)
    for y in years:

        sumPrecipitationYear = cg.sumPrecipitations_byYear(str(y), dicc["daily"]["time"], dicc["daily"]["precipitation_sum"])
        sumPre.append(sumPrecipitationYear)

    for pre in sumPre:
        sum += pre
    media = sum / len(sumPre)



    print(sumPre)

    plt.bar(years, sumPre)
    plt.xlabel("Year")
    plt.ylabel("Suma Precp. Anual (mm)")
    plt.axhline(y=media)

    plt.show()

precipitacionesLast30Years()
