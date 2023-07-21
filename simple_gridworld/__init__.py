from gym.envs.registration import register

register(
    id='SimpleWalk-5-States',
    entry_point='simple_gridworld.envs:SimpleWalkEnv',
    kwargs={'n_states': 5, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)