import gym
env = gym.make('CartPole-v0')
#env = gym.make('MountainCar-v0')
for episode in range(20):
    env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        #print(observation)
        print(reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break