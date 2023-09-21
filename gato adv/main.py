import gym
from gato_env import GatoEnv
import pygame
import numpy as np
from gym import spaces
import stable_baselines3

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
model = A2C('MlpPolicy', env, verbose=0).learn(10000)
    

nombre_archivo_pesos = 'A2C_JugadorPerfecto_10000'
model.save(nombre_archivo_pesos)
