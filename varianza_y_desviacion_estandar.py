# varianza es la diferencia de la media con respecto al cuadrado
# (xi - u)2 / n
import random
import math

from typing import Match

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range (20)]
    mu = media(X)
    var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X = {X}')
    print(f'Media mu: {mu}')
    print(f'Varianza = {var}')
    print(f'Desviacion estandar = {sigma} ')