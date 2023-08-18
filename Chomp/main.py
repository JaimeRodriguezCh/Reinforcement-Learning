import gym
from chomp_env import ChompEnv
import pygame
import numpy as np
from gym import spaces
import stable_baselines3

gym.envs.register(
    id='chomp_env-v0',
    entry_point='chomp_env:ChompEnv',
)
env = gym.make('chomp_env-v0')
obs = env.reset()
env.render()

env = ChompEnv()
observation = env.reset()

done = False
while done==False:
    env.render()
    #action = env.action_space.sample()  # Replace with your agent's action
    user_input = input('Enter space-separated integers: ')
    action = tuple(int(item) for item in user_input.split())
    observation, reward, done, _ = env.step(action)
env.render()
