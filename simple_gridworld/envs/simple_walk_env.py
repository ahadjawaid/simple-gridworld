import gym
import numpy as np
from gym.spaces import Discrete
from gym.envs.toy_text.utils import categorical_sample

class SimpleWalkEnv(gym.Env):
    def __init__(self, n_states=5, p_stay=0.0, p_backward=0.5):
        assert n_states > 2

        self.LEFT, self.RIGHT = 0, 1
        n_actions = 2

        self.first_state = 0
        self.last_state = n_states - 1

        self.start_state = self.current_state = n_states // 2
        self.previous_action = None

        self.observation_space = Discrete(n_states)
        self.action_space = Discrete(n_actions)

        p_forward = 1.0 - (p_stay + p_backward)

        self.P = {}
        for state in range(n_states):
            self.P[state] = {}

            for action in range(n_actions):
                forward_state = self.get_next_state(state, action, direction=1)
                backward_state = self.get_next_state(state, action, direction=-1)

                self.P[state][action] = [
                    (p_forward,  forward_state,  self.get_reward(forward_state),  self.is_done(forward_state)),
                    (p_stay,     state,          self.get_reward(state),          self.is_done(state)),
                    (p_backward, backward_state, self.get_reward(backward_state), self.is_done(backward_state))
                ]

    def get_next_state(self, state: int, action: int, direction: int = 0) -> int:
        next_state = state + direction if (action == self.RIGHT) else state - direction

        return np.clip(self, next_state, self.first_state, self.last_state)

    def get_reward(self, state: int) -> float:
        return -1.0 if (state == self.first_state) else 1.0 if (state == self.last_state) else 0.0

    def is_done(self, state: int) -> bool:
        return bool(state == self.first_state or state == self.last_state)

    def step(self, action):
        possible_transitions = self.P[self.current_state][action]

        probability_index = 0
        resulting_action = [transition[probability_index] for transition in possible_transitions]

        proability, state, reward, is_done = possible_transitions[resulting_action]

        self.current_state = state
        self.previous_action = action

        return (int(state), reward, is_done, {"prob": proability})

    def reset(self):
        self.previous_action = None
        self.current_state = self.start_state