def mejor_movimiento(tablero, jugador):
    def evaluar_estado(tablero):
    # Combinaciones ganadoras en el juego Tic Tac Toe
        combinaciones_ganadoras = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for combinacion in combinaciones_ganadoras:
            valores = [tablero[fila][col] for fila, col in combinacion]
            if valores == [1, 1, 1]:  # Jugador O gana
                return -1
            elif valores == [2, 2, 2]:  # Jugador X gana
                return 1

        for fila in tablero:
            if 0 in fila:
                return None  # El juego no ha terminado

        return 0  # Empate

    def minimax(tablero, profundidad, es_maximizador):
        if evaluar_estado(tablero) == 1:
            return 1
        if evaluar_estado(tablero) == -1:
            return -1
        if evaluar_estado(tablero) == 0:
            return 0

        if es_maximizador:
            mejor_valor = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = jugador
                        valor = minimax(tablero, profundidad + 1, False)
                        tablero[fila][columna] = 0
                        mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            peor_valor = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = 3 - jugador  # Cambiar de jugador
                        valor = minimax(tablero, profundidad + 1, True)
                        tablero[fila][columna] = 0
                        peor_valor = min(peor_valor, valor)
            return peor_valor

    mejor_puntaje = float('-inf')
    mejor_movimiento = -1

    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == 0:
                tablero[fila][columna] = jugador
                puntaje = minimax(tablero, 0, False)
                tablero[fila][columna] = 0

                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_movimiento = fila * 3 + columna

    return mejor_movimiento

# Ejemplo de tablero
tablero_ejemplo = [
    [1, 0, 2],
    [0, 1, 0],
    [0, 2, 2]
]

mejor_mov = mejor_movimiento(tablero_ejemplo, 2)  # Jugador X
print("Mejor movimiento:", mejor_mov)