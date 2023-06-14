# tsp_env.py
import gym
from gym import spaces
from data_loader import load_problem

class TSPEnv(gym.Env):
    def __init__(self, problem_file):
        super(TSPEnv, self).__init__()
        self.n_nodes, self.nodes, self.node_coords, self.problem = load_problem(problem_file)
        self.action_space = spaces.Discrete(self.n_nodes)
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.n_nodes, 2), dtype=float)

    def reset(self):
        self.current_node = self.nodes[0]
        self.visited_nodes = set([self.current_node])
        self.visited_order = [self.current_node]
        return self._get_observation()

    def step(self, action):
        reward = 0
        done = False
        next_node = self.nodes[action]
        if next_node not in self.visited_nodes:
            self.visited_nodes.add(next_node)
            self.visited_order.append(next_node)
            reward = -self.problem.get_weight(self.current_node, next_node)
            self.current_node = next_node
        if len(self.visited_nodes) == self.n_nodes:
            done = True
            reward -= self.problem.get_weight(self.current_node, self.nodes[0])
        return self._get_observation(), reward, done, {}

    def _get_observation(self):
        remaining_nodes = list(set(self.nodes) - self.visited_nodes)
        return [self.node_coords[node] for node in remaining_nodes]

    def render(self, mode='human'):
        print(f"Visited nodes: {self.visited_order}")

    def close(self):
        pass
