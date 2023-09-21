import numpy as np
from función_indices import f_ind
import random 
class Jugador_aleatorio():
    def __init__(self,board,player):
        self.board=board
        self.player=player

    def move(self):
        if self.aviable_mov()==[]:
            tupla = []
        else:
            tupla = random.choice(self.aviable_mov())
        return tupla
    def aviable_mov(self):
        L=[]
        for i in range(3):
            for j in range(3):
                if self.board[i,j]==0:
                    L.append((i,j))
        return L
    def evaluate(self):
        # Verifica filas, columnas y diagonales para encontrar ganadores
        for i in range(3):
            if np.all(self.board[i, :] == 1):
                return 1
            elif np.all(self.board[i, :] == 2):
                return -1
            if np.all(self.board[:, i] == 1):
                return 1
            elif np.all(self.board[:, i] == 2):
                return -1
        if np.all(np.diag(self.board) == 1) or np.all(np.diag(np.fliplr(self.board)) == 1):
            return 1
        elif np.all(np.diag(self.board) == 2) or np.all(np.diag(np.fliplr(self.board)) == 2):
            return -1
        return 0    
'''     
board = np.zeros((3, 3), dtype=int)   
jugador=Jugador_aleatorio()
while jugador.evaluate(board)!=1 or jugador.evaluate(board)!=-1 or np.all(board != 0)==False:
    if(jugador.evaluate(board)==1):
        print('HAS PERDIDO')
        break
    elif(jugador.evaluate(board)==-1):
        print('HAS GANADO')
        break
    elif(np.all(board != 0)==True):
        print('HAS EMPATADO')
        break
    move = jugador.move(board, 1)
    board[move[0]][move[1]]=1
    print(board)
    if jugador.evaluate(board)==1 or jugador.evaluate(board)==-1 or np.all(board != 0)==True:
        if(jugador.evaluate(board)==1):
            print('HAS PERDIDO')
        elif(jugador.evaluate(board)==-1):
            print('HAS GANADO')
        else:
            print('HAS EMPATADO')
        break
    
    input_str = input("Ingrese las coordenadas (fila (1-3),columna (1-3)): ")
    coordinates = f_ind.parse_input(input_str)
    board[coordinates[0]-1,coordinates[1]-1]=2
    print(board)
'''