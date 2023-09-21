import numpy as np

class Jugador_ADV():
    def __init__(self,board,player):
        self.board=board
        self.player=player
        self.cache = {}

    def evaluate(self,board):

        # Verificar si el resultado ya está en la caché
        board_str = str(board)
        if board_str in self.cache:
            return self.cache[board_str]

        # Evaluar el tablero y almacenar el resultado en la caché
        result = 0  # Inicialmente, no hay ganador
        for i in range(3):
            if np.all(board[i, :] == 1):
                result = 1
                break
            elif np.all(board[i, :] == 2):
                result = -1
                break
            if np.all(board[:, i] == 1):
                result = 1
                break
            elif np.all(board[:, i] == 2):
                result = -1
                break
        if np.all(np.diag(board) == 1) or np.all(np.diag(np.fliplr(board)) == 1):
            result = 1
        elif np.all(np.diag(board) == 2) or np.all(np.diag(np.fliplr(board)) == 2):
            result = -1

        # Almacenar el resultado en la caché
        self.cache[board_str] = result
        return result

    def minimax(self, board, depth, is_maximizing, player, alpha, beta):
        if self.evaluate(board) == 1:
            return 1
        if self.evaluate(board) == -1:
            return -1
        if np.all(board != 0):
            return 0

        if is_maximizing:
            max_eval = -np.inf
            for i in range(3):
                for j in range(3):
                    if board[i, j] == 0:
                        board[i, j] = player
                        eval = self.minimax(board, depth + 1, False, player, alpha, beta)
                        max_eval = max(max_eval, eval)
                        board[i, j] = 0
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = np.inf
            for i in range(3):
                for j in range(3):
                    if board[i, j] == 0:
                        board[i, j] = 3 - player  # Cambiar al otro jugador
                        eval = self.minimax(board, depth + 1, True, player, alpha, beta)
                        min_eval = min(min_eval, eval)
                        board[i, j] = 0
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def best_move(self):
        best_val = -np.inf
        move = None
        alpha = -np.inf
        beta = np.inf
        c=0
        for i in range(3):
            for j in range(3):
                if self.board[i,j]!=0:
                    c=c+1
                if c==9:
                    return []

        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    self.board[i, j] = self.player
                    move_val = self.minimax(self.board, 0, False, self.player, alpha, beta)
                    self.board[i, j] = 0
                    if move_val > best_val:
                        best_val = move_val
                        move = (i, j)
                    alpha = max(alpha, move_val)
        
        return move

# Ejemplo de uso
board = np.zeros((3, 3), dtype=int)
jugador = Jugador_ADV(board,1)

while jugador.evaluate(board) == 0 and not np.all(board != 0):
    #jugador = Jugador_ADV(board,1)
    print(board)
    input_str = input("Ingrese las coordenadas (fila (1-3), columna (1-3)): ")
    coordinates = [int(x) for x in input_str.split()]
    board[coordinates[0] - 1, coordinates[1] - 1] = 2
    print(board)

    move = jugador.best_move()
    board[move[0]][move[1]] = 1
    print(board)
    if jugador.evaluate(board) != 0 or np.all(board != 0):
        break


''' 
board=np.zeros((3,3),dtype=int)

print(board)
jugador = Jugador_ADV(board,1)
print(jugador.best_move())
M=jugador.best_move()

print(board)
'''