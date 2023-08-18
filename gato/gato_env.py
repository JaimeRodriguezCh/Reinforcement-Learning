import gym 
from gym import spaces
import numpy as np
#from gym_gato.envs.gato import Gato

class GatoEnv(gym.Env):
    def __init__(self):
        # Definir el espacio de observación y de acción
        self.board = np.zeros((3, 3), dtype=int)  # Tablero 3x3
        self.action_space = spaces.Discrete(9)    # 9 posiciones para marcar
        self.observation_space = spaces.Box(low=0, high=1, shape=(3, 3), dtype=int)

        self.current_player = 1  # Jugador 1 comienza
        self.winner = None

    
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.winner = None
        return self.board

    def step(self, action):
        row, col = action // 3, action % 3

        if self.board[row, col] != 0:
            return self.board, -10, False, {}  # Movimiento inválido, penalización

        self.board[row, col] = self.current_player

        if self._check_winner(self.current_player):
            self.winner = self.current_player
            return self.board, 1, True, {}

        if np.all(self.board != 0):
            return self.board, 0, True, {}  # Empate

        self.current_player = 3 - self.current_player  # Alternar jugadores
        return self.board, 0, False, {}

    def render(self, mode='human'):
        if mode == 'human':
            print(self.board)

    def _check_winner(self, player):
        # Lógica para verificar si el jugador actual ha ganado
        # Implementación de las combinaciones ganadoras (filas, columnas, diagonales)
        # Comprobar filas y columnas
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        
        # Comprobar diagonales
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True

        return False
        

    def close(self):
        pass  # Puede ser utilizado para liberar recursos si es necesario
 