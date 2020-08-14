# Summary: On Local Rewards and Scaling Distributed Reinforcement Learning

- Independent agents optimize joint performance metric

=> *Problems with such factorizations where the global reward decomposes in to a sum of local rewards*

- local information can dramatically reduce the number of examples necessary for learning to O(log n)

- estimate model parameters from all local information available, and then to solve the resulting model offline

- Dynamic Bayes Net (DBN)-MDP => neigh(i): subset of agents that i’s state directly influences

- agent i’s state is directly influenced by the states of neigh(i) but not their actions

- policies in which agent i chooses its local action as function of only its local state s(i) (and possibly its neighbors); in this case, policy of i can be restricted to depend only on s(i)

- local and global reward function