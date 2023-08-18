import gym
from gym import spaces
import numpy as np

class ChompEnv(gym.Env):
    def __init__(self, board_size=(5, 5)):
        super(ChompEnv, self).__init__()

        self.board_size = board_size
        self.action_space = spaces.Tuple((spaces.Discrete(board_size[0]), spaces.Discrete(board_size[1])))
        self.observation_space = spaces.Box(low=0, high=1, shape=board_size, dtype=int)

        self.board = np.ones(board_size, dtype=int)
        self.reset()

    def reset(self):
        self.board = np.ones(self.board_size, dtype=int)
        self.board[0, 0] = 0  # The starting player removes the top-left square
        self.player_turn = 0
        self.done = False
        return self.board.copy()

    def step(self, action):
        row, col = action

        if self.done or self.board[row, col] == 0:
            return self.board.copy(), 0, True, {}

        self.board[row:, col:] = 0
        self.done = (np.sum(self.board) == 0)
        reward = 1 if self.player_turn == 1 else -1
        self.player_turn = 1 - self.player_turn

        return self.board.copy(), reward, self.done, {}

    def render(self, mode='human'):
        for row in self.board:
            print(' '.join(['*' if val == 1 else ' ' for val in row]))