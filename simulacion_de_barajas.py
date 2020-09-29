import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas

def obntener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obntener_mano(barajas, tamano_mano)
        manos.append(mano)
    pares = 0

    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        Counter = dict(collections.Counter(valores))
        for val in Counter.values():
            if val == 5:
                pares += 1
                break

    probabilidad_par = pares/intentos
    print(f'La probabilidad de obtener una mano de  {tamano_mano} es de {probabilidad_par}')

if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    
    main(tamano_mano, intentos)
    