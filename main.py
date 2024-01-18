import sys
import grafics_gava as gg

def help():
    print("adeu")

def graficas(numEstudio):

    if numEstudio == 1:
        gg.barGraph_precipitaciones_Last30Years()


def main():
    args = sys.argv

    if len(args) != 2:
        print("ERROR. DEBE HABER ÚNICAMENTE UN ARGUMENTO")
    else:
        num = args[1].strip()[-1]
        if args[1].lower() == "help":
            help()

        elif args[1].lower() == f"estudio_{num}":
            if num in ["1", "2", "3", "4", "5", "6"]:
                graficas(int(num))
            else:
                print("Opcion no válida")

        else:
            print("Opcion no válida")

main()