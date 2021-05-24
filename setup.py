from setuptools import setup, find_packages

setup(name='generative_playing_networks',
	version='0.0.1',
	packages= find_packages(),
	install_requires=['gym>=0.10.5', 'numpy>=1.13.3', 'tensorboard==1.14','tensorboardX>=2.0', 'pandas>=0.25.0'])