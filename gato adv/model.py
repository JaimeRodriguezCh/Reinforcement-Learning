import gym
from gato_env import GatoEnv
import pygame
import numpy as np
from gym import spaces
import stable_baselines3
from Jugador_Random import Jugador_aleatorio
from función_indices import f_ind

# Register the environment

gym.register(
    id='gato_env-v0',
    entry_point='gato_env:GatoEnv'
)

# Test the environment
env = gym.make('gato_env-v0')
obs = env.reset()
env.render()
env = GatoEnv()
done = False
#from stable_baselines3.common.env_checker import check_env
#check_env(env, warn=True)

from stable_baselines3 import DQN, PPO, A2C, DDPG, SAC, TD3


# Instantiate the env

env = GatoEnv()

model = A2C.load('lo_mejor_hasta_ahora', env=env)
obs = env.reset()

while env._check_winner(1)==False and env._check_winner(2)==False and np.all(env.board != 0)==False:
    if(env._check_winner(1)):
        print('HAS PERDIDO')
        break
    elif(env._check_winner(2)):
        print('HAS GANADO')
        break
    elif(np.all(env.board != 0)==True):
        print('HAS EMPATADO')
        break
    move, _ = model.predict(obs, deterministic=True)
    row, col = move // 3, move % 3
    env.board[row,col]=2
    print(env.board)
    if env._check_winner(1) or env._check_winner(2) or np.all(env.board != 0)==True:
        if(env._check_winner(1)):
          print('HAS PERDIDO')
          break
        elif(env._check_winner(2)):
            print('HAS GANADO')
            break
        elif(np.all(env.board != 0)==True):
            print('HAS EMPATADO')
            break
    
    input_str = input("Ingrese las coordenadas (fila (1-3),columna (1-3)): ")
    coordinates = f_ind.parse_input(input_str)
    env.board[coordinates[0]-1,coordinates[1]-1]=1
    '''
    Entrenador=Jugador_aleatorio(env.board,2)
    if Entrenador.move()!=[]:
        Emove=Entrenador.move()
        env.board[Emove[0],Emove[1]]=2
    print(env.board)'''
    if env._check_winner(1) or env._check_winner(2) or np.all(env.board != 0)==True:
        if(env._check_winner(1)):
          print('HAS PERDIDO')
          break
        elif(env._check_winner(2)):
            print('HAS GANADO')
            break
        elif(np.all(env.board != 0)==True):
            print('HAS EMPATADO')
            break