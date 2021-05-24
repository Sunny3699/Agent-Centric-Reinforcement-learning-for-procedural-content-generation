<h1 align="center">
  Agent centric Reinforcement Learning for PCG
</h1>

## About the project ##
A Level generator which when given a game portrayed in Video Game Description Language (VGDL) and which can be played by some AI player, constructs any necessary number of various levels for that game which are enjoyable for humans to play.

## Basic Requirements ##
1. Linux Environment
2. Anaconda for Linux
3. GPU(We trained it on 6GB NVIDIA RTX 2070 MAX-Q)
4. Pytorch


## Installation Instructions ##

1. Go to the root of this directory after cloning the project to your local environment.
2. `pip install -e .`
3. To install GVGAI game environments, follow <br/>
`git clone https://github.com/rubenrtorrado/GVGAI_GYM.git` <br/>
`cd GVGAI_GYM`<br/>
`pip install -e .`
4. To install the RL libraries and dependencies <br/>
`git clone https://github.com/openai/baselines.git`<br/>
`cd baselines`<br/>
`pip install -e .`
5. To install the Pytorch version of A2C, PPO, ACKTR, GAIL <br/>
`git clone https://github.com/ikostrikov/pytorch-a2c-ppo-acktr-gail.git` <br/>
`cd pytorch-a2c-ppo-acktr-gail`<br/>
`pip install -e .`

6. Now please go to the root of this directory and run,<br/>
`python run.py`

## Some screenshots as the training progresses ##
<p align="center">
    <img src="Generated levels/1.png"
    height="15%" width="15%">
   <img src="Generated levels/2.png"
    height="15%" width="15%">
   <img src="Generated levels/3.png"
    height="15%" width="15%">
   <img src="Generated levels/4.png"
    height="15%" width="15%">
   <img src="Generated levels/5.png"
    height="15%" width="15%">
   <img src="Generated levels/6.png"
    height="15%" width="15%">
</p>


## Contributed with ❤ by ##

 [Kalyan Valiveti](https://github.com/kalyan-v)<br/>
 [Sunny Bommasani](https://github.com/Sunny3699)
