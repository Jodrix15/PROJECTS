import grafics_gava as gg
import sys

def help():
    print("[estudio_1] - Gráfico de barras de los últimos 30 años")


def estudio(opcion):

    if opcion == "1":
        gg.barGraph_precipitaciones_Last30Years()
    else:
        print("Opcion no válida")


def main():
    args = sys.argv
    opcion = args[1][-1]

    if args[1].lower() == "help":
        help()

    elif args[1].lower() == f"estudio_{opcion}":
        estudio(opcion)
    else:
        print("Opcion no válida")


main()