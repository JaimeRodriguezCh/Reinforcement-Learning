class TicTacToePlayer:
    def __init__(self):
        self.PLAYER = 'X'
        self.OPPONENT = 'O'
    
    def minimax(self, board, depth, is_maximizing):
        score = self.evaluate(board)
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if not any([cell == '-' for cell in board]):
            return 0
    
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == '-':
                    board[i] = self.PLAYER
                    score = self.minimax(board, depth + 1, not is_maximizing)
                    board[i] = '-'
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '-':
                    board[i] = self.OPPONENT
                    score = self.minimax(board, depth + 1, not is_maximizing)
                    board[i] = '-'
                    best_score = min(score, best_score)
            return best_score
    
    def find_best_move(self, board):
        best_move = -1
        best_score = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = self.PLAYER
                move_score = self.minimax(board, 0, False)
                board[i] = '-'
                if move_score > best_score:
                    best_score = move_score
                    best_move = i
        return best_move
    
    def evaluate(self, board):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
    
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]]:
                if board[combo[0]] == 'X':
                    return 10
                elif board[combo[0]] == 'O':
                    return -10
        return 0

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])

def main():
    player = TicTacToePlayer()
    board = ['-'] * 9
    while True:
        user_input = input('Enter space-separated integers (1-3) (1-3): ')
        action = tuple(int(item) for item in user_input.split())
        player_move = (action[0] - 1) * 3 + (action[1] - 1)


        if board[player_move] == '-':
            board[player_move] = 'O'
            print_board(board)
            if player.evaluate(board) == -10:
                print("¡Has ganado!")
                break
            computer_move = player.find_best_move(board)
            board[computer_move] = 'X'
            print("Movimiento de la computadora:")
            print_board(board)
            if player.evaluate(board) == 10:
                print("¡La computadora ha ganado!")
                break
            elif not any([cell == '-' for cell in board]):
                print("¡Empate!")
                break

if __name__ == "__main__":
    main()
