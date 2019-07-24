import gym
import numpy as np

env = gym.make('FrozenLake-v0')

#Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])

# Set learning parameters
lr = .8
y = .95
EPSILON = 0.9
num_episodes = 2000

for i in range(num_episodes):
    #Reset environment and get first new observation
    s = env.reset()
    d = False
    j = 0

    #The Q-Table learning algorithm
    while j < 99:
        j+=1

        #Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))

        #Get new state and reward from environment
        s1,r,d,_ = env.step(a)

        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        s = s1
        if d == True:
            break

print("Final Q-Table Values")
print(Q)