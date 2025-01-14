import numpy as np
import random

class RLAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = {}

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)
        else:
            return max(self.actions, key=lambda action: self.q_table.get((state, action), 0))

    def update_q_value(self, state, action, reward, next_state):
        old_value = self.q_table.get((state, action), 0)
        next_max = max([self.q_table.get((next_state, a), 0) for a in self.actions], default=0)
        new_value = (1 - self.learning_rate) * old_value + \
                    self.learning_rate * (reward + self.discount_factor * next_max)
        self.q_table[(state, action)] = new_value

if __name__ == "__main__":
    actions = [-50, -25, 0, 25, 50]  # Clock speed adjustments in MHz
    agent = RLAgent(actions)
    state = (80, 70, 150)  # Example state (temperature, utilization, power)
    action = agent.choose_action(state)
    print(f"Chosen action: {action}")
    agent.update_q_value(state, action, reward=10, next_state=(75, 65, 140))
