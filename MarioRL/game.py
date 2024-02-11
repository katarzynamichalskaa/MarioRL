from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from gym.wrappers import GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from matplotlib import pyplot as plt

#Create the base environment
env = gym_super_mario_bros.make('SuperMarioBros-v0')
#Simplify the controls
env = JoypadSpace(env, SIMPLE_MOVEMENT)

'''
#Grayscale
env = GrayScaleObservation(env, keep_dim=True)
#Wrap inside the Dummy
env = DummyVecEnv([lambda: env])
#Stack the frames
env = VecFrameStack(env, 4, channels_order='last')
'''

done = True
# Main loop
for step in range(5000):
    #Start the game to begin with
    if done:
        #Start the game
        env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    #Show game on the screen
    env.render()
env.close()


