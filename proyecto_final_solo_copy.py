import random

def imprime_tablero(lista_asteriscos):
    num = 0
    print('      0     1     2     3     4     5')
    print('   ------------------------------------')
    for i in lista_asteriscos:       
        print(num,' | ', end='')
        for j in i:
            length = len(str(j))
            if length == 1:
                print(j, end='     ')
            elif length == 2:
                print(j, end='    ')
            else:
                print(j, end='    ')
        print('\n')
        num += 1

def genera_lista():

    lista = []
    for i in range(1,19):
        lista.append(i)
        lista.append(i)
    random.shuffle(lista)
    
    lista_final = []
    temporal = []

    for i in lista:
        if len(temporal) == 6:
            lista_final.append(temporal)
            temporal = [i]
        else:
            temporal.append(i)
    lista_final.append(temporal)
    
    return lista_final

def seleccionar_cartas(jugador, lista, lista_seleccionados):

    print('Turno de jugador ', jugador)

    while True:
        carta1 = []
        while True:
            try:
                carta1.append(int(input('Renglon de carta 1 deseada: ')))
                break
            except:
                print('Error')

        while True:
            try:
                carta1.append(int(input('Columna de carta 1 deseada: ')))
                break
            except:
                print('Error')

        if lista[carta1[0]][carta1[1]] in lista_seleccionados:
            print('Esta carta ya fue seleccionada')
        else:
            break

    print('La carta es: ', lista[carta1[0]] [carta1[1]])
    
    while True:
        carta2 = []
        while True:
            try:
                carta2.append(int(input('Renglon de carta 2 deseada: ')))
                break
            except:
                print('Error')

        while True:
            try:
                carta2.append(int(input('Columna de carta 2 deseada: ')))
                break
            except:
                print('Error')

        if lista[carta2[0]] in lista_seleccionados or lista[carta2[0]][carta2[1]] in lista_seleccionados:
            print('Esta carta ya fue seleccionada')
        elif carta1 == carta2:
            print('No puede ser igual que la carta 1')
        else:
            break

    print('La carta es: ', lista[carta2[0]] [carta2[1]])

    return carta1, carta2

def verificar_cartas(lista, lista_asteriscos, lista_seleccionados, carta1, carta2, jugador, puntuaje1, puntuaje2):
    carta_seleccionada1 = lista[carta1[0]] [carta1[1]]
    carta_seleccionada2 = lista[carta2[0]] [carta2[1]]

    if carta_seleccionada1 == carta_seleccionada2 and carta_seleccionada1 not in lista_seleccionados:
        lista_seleccionados.append(carta_seleccionada1)
        lista_asteriscos[carta1[0]][carta1[1]] = carta_seleccionada1
        lista_asteriscos[carta2[0]][carta2[1]] = carta_seleccionada2
        if jugador == 1:
            puntuaje1 += 1
            jugador = 1
        elif jugador == 2:
            puntuaje2 += 1
            jugador = 2
        print('Las cartas son par')
    else:
        print('Las cartas no son par')
        if jugador == 1:
            jugador = 2
        elif jugador == 2:
            jugador = 1

    return lista_asteriscos, lista_seleccionados, jugador, puntuaje1, puntuaje2

def main():

    lista_asteriscos = [
        ['--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--']
    ]

    print('----Bienvenido al juego de memoria----')
    print()

    lista = genera_lista()
    lista_seleccionados = []
    jugador = 1
    puntuaje1 = 0
    puntuaje2 = 0


    while puntuaje1 + puntuaje2 < 18:
        print(lista)
        imprime_tablero(lista_asteriscos)
        carta1, carta2 = seleccionar_cartas(jugador, lista, lista_seleccionados)
        lista_asteriscos, lista_seleccionados, jugador, puntuaje1, puntuaje2 = verificar_cartas(lista, lista_asteriscos, lista_seleccionados, carta1, carta2, jugador, puntuaje1, puntuaje2)
        
        if puntuaje1 > puntuaje2 and puntuaje1 + puntuaje2 == 18:
            print('¡Ganó el jugador 1!')
        elif puntuaje2 > puntuaje1 and puntuaje1 + puntuaje2 == 18:
            print('¡Ganó el jugador 2!')
        else:
            pass

    imprime_tablero(lista_asteriscos)

main()