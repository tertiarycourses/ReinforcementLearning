import gym
env = gym.make('CartPole-v0')
# env = gym.make('MountainCar-v0')
env.reset()
for _ in range(100):
    env.render()
    # action = env.action_space.sample()
    # env.step(action)
