import math as m
import numpy as np
import matplotlib.pyplot as plt

def graficoPuntos():
    ejeX = [2006 + x for x in range(16)]
    ejeY = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]

    plt.scatter(ejeX, ejeY, c="red", marker="*")
    # c para cambiar el color de la grafica
    # podemos poner el nombre del color, o el código
    #marker -> forma de los puntos
    #alpha -> transparencia
    #s -> tamaño
    plt.show()

def graficoLinea():
    ejeX = [2006 + x for x in range(16)]
    ejeY = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]

    plt.plot(ejeX, ejeY)
    plt.show()

def grafBarras():

    ejeX = ["pikachu", "charmander", "growlithe", "squirtle", "bulbasaur"]
    ejeY = [25, 50, 80, 45, 30]

    plt.bar(ejeX, ejeY)
    #width -> ancho
    #align -> borde
    #plt.bar(ejeX, ejeY, width=0.5)
    plt.show()

def grafHistograma():
    ages = np.random.normal(20, 1.5, 1000)
    plt.hist(ages)
    plt.show()

def grafQuesos():
    langs = ["Python", "C++", "Java", "C#", "Go"]
    votes = [50, 30, 24, 79, 44]
    explodes = [0, 0, 0.2, 0, 0]

    #explode -> separa cada uno de los quesitos tanto como el valor indicado
    plt.pie(votes, labels=langs, explode=explodes)
    #plt.pie(votes, labels=langs)
    plt.show()


#graficoPuntos()
#graficoLinea()
#grafBarras()
grafHistograma()
#grafQuesos()


