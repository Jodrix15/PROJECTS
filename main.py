import grafics_gava as gg
import sys

def help():
    print("\nEscribe el 'estudio_X' para mostrar el gráfico correspondiente:\n\n"
          "estudio_1 - Suma y media de las precipitaciones de los últimos 30 años (En grupo)\n"
          "estudio_2 - % de precipitaciones en tres décadas aisladas (En grupo)\n"
          "estudio_3 - Temperaturas medias en los últimos 30 años (En grupo)\n"
          "estudio_4 - Evolución de la temperatura desde los años 70 en tres décadas aisladas (En grupo)\n"
          "estudio_5 - Top 3 de las temperaturas más altas y más bajas en los últimos 30 años (Jordi)\n")


def estudio(opcion):

    if opcion == "1":
        gg.barGraph_precipitaciones_Last30Years()
    elif opcion == "2":
        gg.pieGraph_mediaPrecp_50vs70vsLast10()
    elif opcion == "3":
        gg.barGraphTempMed_Last30Years()
    elif opcion == "4":
        gg.plotGraph_tempEvolution_70vs90vsLast10Years()
    elif opcion == "5":
        gg.top3Graph_TempMediaMasAltaYBaja_last30Years()
    else:
        print("Opcion no válida")


def main():
    args = sys.argv
    opcion = args[1][-1]

    if len(args) != 2:
        print("ERROR. DEBE CONTENER ÚNICAMENTE UN ARGUMENTO")
    else:
        if args[1].lower() == "help":
            help()

        elif args[1].lower() == f"estudio_{opcion}":
            estudio(opcion)

        else:
            print("Opcion no válida")

main()