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
model = A2C('MlpPolicy', env, verbose=1).learn(50000)

# Test the trained agent
obs = env.reset()
c = 0
while done==False:
  action, _ = model.predict(obs, deterministic=True)
  print("Step {}".format(c + 1))
  c=c+1
  print("Action: ", action)
  obs, reward, done, info = env.step(action, mode='human')
  print('obs=', obs, 'reward=', reward, 'done=', done)
  env.render(mode='console')
  if done:
    # Note that the VecEnv resets automatically
    # when a done signal is encountered
    print("Goal reached!", "reward=", reward)
    break
    

