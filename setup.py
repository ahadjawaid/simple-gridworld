from setuptools import setup

setup(name='simple_gridworld',
      version='0.01',
      description='Simple Gridworld - Used to learn how to create an environment',
      url='https://github.com/ahadjawaid/simple-gridworld',
      author='Ahad Jawaid',
      packages=['simple_gridworld', 'simple_gridworld.envs'],
      author_email='',
      license='MIT License',
      install_requires=['gym>=0.2.3'],
)