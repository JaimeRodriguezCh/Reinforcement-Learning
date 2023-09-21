import gym 
from gym import spaces
import numpy as np
import random
#from gym_gato.envs.gato import Gato

class GatoEnv(gym.Env):
    def __init__(self):
        # Definir el espacio de observación y de acción
        self.board = np.zeros((3, 3), dtype=int)  # Tablero 3x3
        self.action_space = spaces.Discrete(9)    # 9 posiciones para marcar
        self.observation_space = spaces.Box(low=0, high=2, shape=(3, 3), dtype=int)
        self.winner = None

    
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.winner = None
        return self.board
    def aviable_mov(self):
        L=[]
        for i in range(3):
            for j in range(3):
                if self.board[i,j]==0:
                    L.append((i,j))
        return L


    def step(self, action, mode = 'random'):

        row, col = action // 3, action % 3

        if self.board[row, col] != 0:
            return self.board, -10, False, {}  # Movimiento inválido, penalización
        self.board[row, col] = 1

        if mode == 'random':
            if self.aviable_mov() != []:
                rowo, colo = random.choice(self.aviable_mov())
                self.board[rowo,colo]=2
        elif mode == 'human':
            accion=int(input('ingrese movimiento'))
            row, col = accion // 3, accion % 3
            self.board[row, col] = 2

        if self._check_winner(1):
            self.winner = 1
            return self.board, 1, True, {}
        if self._check_winner(2):
            self.winner = 2
            return self.board, -1, True, {}

        if np.all(self.board != 0):
            return self.board, 0, True, {}  # Empate

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
 