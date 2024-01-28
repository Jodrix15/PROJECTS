import grafics_gava as gg
import sys

def help():
    print("\nEscribe el 'estudio_X' para mostrar el gráfico correspondiente:\n\n"
          "estudio_1 - Suma y media de las precipitaciones de los últimos 30 años (En grupo)\n"
          "estudio_2 - % de precipitaciones en tres décadas aisladas (En grupo)\n"
          "estudio_3 - Evolución de la temperatura desde los años 70 en tres décadas aisladas (En grupo)\n"
          "estudio_4 - Temperaturas medias en los últimos 30 años (David)\n"
          "estudio_5 - Top 3 de las temperaturas más altas y más bajas en los últimos 30 años (Jordi)\n"
          "estudio_6 - Evolución de las temperaturas por estaciones en diferentes décadas (Santi)\n"
          "estudio_7 - Evolución de las temperaturas medias en el día de Navidad desde el 1990 (Marcos)\n")


def estudio(opcion):

    if opcion == "1":
        gg.barGraph_precipitaciones_Last30Years()
    elif opcion == "2":
        gg.pieGraph_mediaPrecp_50vs70vsLast10()
    elif opcion == "3":
        gg.plotGraph_tempEvolution_70vs90vsLast10Years()
    elif opcion == "4":
        gg.barGraphTempMed_Last30Years()
    elif opcion == "5":
        gg.top3Graph_TempMediaMasAltaYBaja_last30Years()
    elif opcion == "6":
        gg.barGraph_EstacionesEvolucion_70vs90vs20vsLast10Years()
    elif opcion == "7":
        gg.plotGraph_temperaturasMedias_enNavidad_last30Years()
    else:
        print("Opcion no válida")


def main():
    args = sys.argv

    if len(args) != 2:
        print("ERROR. DEBE CONTENER ÚNICAMENTE UN ARGUMENTO")
    else:
        opcion = args[1][-1]
        if args[1].lower() == "help":
            help()

        elif args[1].lower() == f"estudio_{opcion}":
            estudio(opcion)

        else:
            print("Opcion no válida")

main()