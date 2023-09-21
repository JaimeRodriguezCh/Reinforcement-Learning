import random
agente = 1
oponente = -1
vacio = 0

class Gato:
    def __init__(self, estado_de_juego=None):
        if estado_de_juego is None:
            estado_de_juego = [
                0, 0, 0,
                0, 0, 0,
                0, 0, 0
            ]
        self.estado = estado_de_juego

    def __str__(self):
        return str(self.estado)

    def llenito(self):
        return len([bloque for bloque in self.estado if bloque == vacio]) == 0

    def termino(self):
        return self.obtener_ganador() != vacio or self.llenito()

    def movimientos_posibles(self):
        return [i for i in range(9) if self.estado[i] == vacio]

    def movimientol(self, bloque, jugador):
        jugada = list(self.estado)
        jugada[bloque] = jugador
        return Gato(jugada)

    def obtener_ganador(self):
        estado = self.estado
        for i in range(3):
            if estado[i * 3] == estado[i * 3 + 1] == estado[i * 3 + 2] == estado[i * 3] != vacio:
                return estado[i * 3]
            if estado[i] == estado[i + 3] == estado[i + 6] == estado[i] != vacio:
                return estado[i]
            if estado[0] == estado[4] == estado[8] == estado[0] != vacio:
                return estado[0]
            if estado[2] == estado[4] == estado[6] == estado[2] != vacio:
                return estado[2]

        return vacio
def simulador(politica_del_agente, politica_del_oponente, num_de_simulaciones=100):
    juegos_ganados = 0
    empatados = 0
    # simular
    for i in range(num_de_simulaciones):
        juego = Gato()
        # 50% de que el oponente juegue
        if random.random() > 0.5:
            juego = juego.movimientol(politica_del_oponente(juego), oponente)

        while not juego.termino():
            # primero empieza el agente
            juego = juego.movimientol(politica_del_agente(juego), agente)
            if juego.termino():
                break
            # si no juega el oponente
            movimiento = juego.movimientol(politica_del_oponente(juego), oponente)

        if juego.obtener_ganador() == 0:
            empatados = empatados + 1
        if juego.obtener_ganador() > 0:
            juegos_ganados = juegos_ganados + 1

    return juegos_ganados, empatados
def reward(juego):
    return max(juego.obtener_ganador(), 0)
class Valor_politica:
    valor_por_defecto = 0.5

    def __init__(self):
        self.valores = {}

    def politica(self, juego):
        valor_movimientos = {}
        movimientos = juego.movimientos_posibles()
        for movimiento in movimientos:
            jugada = juego.movimientol(movimiento, agente)
            valor_movimientos[movimiento] = self.obtener_valor_del_estado(jugada)

        return max(valor_movimientos, key=valor_movimientos.get)

    def obtener_valor_del_estado(self, estado):
        if str(estado) not in self.valores:
            return self.valor_por_defecto
        return self.valores[str(estado)]

    def conjunto_de_valores_de_estados(self, estado, valor):
        self.valores[str(estado)] = valor

    def aprende(self, estados):

        def temporal_difference(valor_estado_actual, valor_estado_siguiente):
            learning_rate = 0.1
            return valor_estado_actual + learning_rate * (valor_estado_siguiente - valor_estado_actual)

        estado_anterior = estados[-1:][0]
        valor_anterior = reward(estado_anterior)
        self.conjunto_de_valores_de_estados(estado_anterior, valor_anterior)
        # Pasar por todos los estados desde principio al fin
        for estado in reversed(estados[:-1]):
            valor = self.obtener_valor_del_estado(estado)
            valor_anterior = temporal_difference(valor, valor_anterior)
            self.conjunto_de_valores_de_estados(estado, valor_anterior)
def politica_random(juego):
    return random.choice(juego.movimientos_posibles())
def entrenamiento(politica, politica_del_oponente, training_games=1000):
    for i in range(training_games):
        juego = Gato()
        estados = []

        # 50% que el oponente empiece
        if random.random() > 0.5:
            juego = juego.movimientol(politica_del_oponente(juego), oponente)

        while not juego.termino():
            # el agente hace un movimiento con la politica pero ocasionalmente hace uno aleatorio
            if random.random() < 0.5:
                juego = juego.movimientol(politica_random(juego), agente)
            else:
                juego = juego.movimientol(politica.politica(juego), agente)
            estados.append(juego)

            if juego.termino():
                break

            juego = juego.movimientol(politica_del_oponente(juego), oponente)
            estados.append(juego)

        politica.aprende(estados)
politica = Valor_politica()

entrenamiento(politica, politica_random, training_games=1000)

games_to_play = 100000
games_won, draw = simulador(politica.politica, politica_random, games_to_play)

print("Games played: %s" % games_to_play)
print("Games won: %s" % games_won)
print("Draw: %s" % draw)