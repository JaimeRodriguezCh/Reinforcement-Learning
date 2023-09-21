import gym 
from gym import spaces
import numpy as np
import random
#from Jugador_Random import Jugador_aleatorio
from Jugador_Adversarial import Jugador_ADV
#from gym_gato.envs.gato import Gato
from función_indices import f_ind

class GatoEnv(gym.Env):
    def __init__(self):
        # Definir el espacio de observación y de acción
        self.n=3
        self.board = np.zeros((self.n, self.n), dtype=int)  # Tablero 3x3
        self.action_space = spaces.Discrete(self.n*self.n)    # 9 posiciones para marcar
        self.observation_space = spaces.Box(low=0, high=2, shape=(self.n, self.n), dtype=int)
        self.winner = None
        self.Turno = False # cuando es False, no se modifica el entorno, cuando es True se modifica el entorno 
        self.c=0
    
    
    def reset(self):
        self.board = np.zeros((self.n, self.n), dtype=int)
        self.winner = None
        self.Turno=False
        #self.c=0
        return self.board
    
    def step(self, action):
        self.c=self.c+1
        if self.c % 1000 ==0:
            print(self.c)

        row, col = action // 3, action % 3

        if self.board[row, col] != 0:
            #print(self.board)
            return self.board, -1, False, {}  # Movimiento inválido, penalización
        
        elif self.Turno==False:
            #juega 1
            self.board[row, col] = 2
            self.Turno=True
            #print(self.board)

        # 'juega' 2 si esque aun no hay algun ganador o si es empate
        Entrenador=Jugador_ADV(self.board,1)
        
        if Entrenador.best_move()!=[] and self.Turno==True and self._check_winner(2)==False:
            #print(self.board)
            move2 = Entrenador.best_move() # entrenador modifica el entorno para ver que hace su pupilo
            self.board[move2[0]][move2[1]]=1
            self.Turno=False
            
        #print(self.board)
        
        if self._check_winner(1):
            self.winner = 1
            #print('BIEN')
            #print(self.board)
       
            return self.board, 1, True, {}
        if self._check_winner(2):
            self.winner = 2
            #print(self.board)
            #print('MAL')
       
            return self.board, -1, True, {}

        if np.all(self.board != 0):

            #print('APRENDIÓ')
            #print(self.board)
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

'''
juego=GatoEnv()

while juego._check_winner(1)==False and juego._check_winner(2)==False and np.all(juego.board != 0)==False:
    print(juego.board)
    if(juego._check_winner(2)):
        print('HAS PERDIDO')
        break
    elif(juego._check_winner(1)):
        print('HAS GANADO')
        break
    elif(np.all(juego.board != 0)==True):
        print('HAS EMPATADO')
        break

    action = int(input("Ingrese las coordenadas 0-8"))


    juego.step(action)
    print(juego.board)

'''