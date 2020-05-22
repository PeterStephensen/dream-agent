import random, math, matplotlib.pyplot as plt, numpy as np

from dream_agent import Agent

from event import *
from settings import *
from person import *
from statistics import *
from simulation import *
from ecommunication import *


Settings.number_of_agents = 1000
Settings.number_of_periods = 10000
Settings.out_file = "test.txt"

Settings.graphics_show = True
Settings.graphics_periods_per_pic = 25

Settings.loot_share = 0.25 # If you win, this is the share of the others wealth you get
Settings.attack_probability = 0.1

Simulation()

print("ok")