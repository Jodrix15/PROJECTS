
def menuWelcome():
    print("\n=======BIENVENIDO AL POKEHORCADO=======")

def menuGen():
    print("\nElige la generación Pokémon con la que quieras jugar\n(solo saldrán pokémons de esa generación):\n\n"+
          "1. Primera Generación\n"
          "2. Segunda Generación\n"
          "3. Tercera Generación\n"
          "4. Cuarta Generación\n"
          "5. Todas las anteriores\n"
          "6. Salir\n")

def menuDifficulty():
    print("\n1. Fácil\n"
          "2. Normal\n"
          "3. Difícil\n"
          "4. Ayuda\n"
          "5. Salir\n")

def help():
    print("\nLos modos de dificultad tienen las siguientes características:\n"
          "\t- Se pierde una vida cuando no se acierta.")
    print("\nEn fácil:\n"
          "\t- 3 Pistas\n"
          "\t- 6 Vidas\n"
          "\t- Se muestran las letras dichas\n"
          "\t- NO se pierden vidas por repetir letras\n\n"
          "En normal:\n"
          "\t- 2 Pistas\n"
          "\t- 5 Vidas\n"
          "\t- NO se muestras las letras dichas\n"
          "\t- NO se pierden vidas por repetir letras\n\n"
          "En difícil:\n"
          "\t- 1 Pistas(elegible entre 2, el id del pokémon o el tipo del mismo)\n"
          "\t- 3 Vidas\n"
          "\t- No se muestran las letras dichas\n"
          "\t- Se pierden vidas por repetir letras\n\n")

def menu(pistasDisponibles):
    print("\n1. Adivinar Pokémon\t\t"
          "2. Decir Letra\n"
          f"3. Pista (Disponibles: {pistasDisponibles})\t"
          "4. Salir\n")

def menuOculto():
      print("Hola Jugador, has entrado en un modo de juego oculto. En este modo de juego\n"
            "jugarás en modo difícil y solo hay 6 pokémon.\n")