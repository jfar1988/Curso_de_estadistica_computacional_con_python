import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numer_de_intentos):
    tiros = []
    for _ in range(numer_de_intentos):
        secuancia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuancia_de_tiros)
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    probabilidad_tiros_con_1 = tiros_con_1/numer_de_intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} de tiros = {probabilidad_tiros_con_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numer_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numer_de_intentos)