# import random, math, matplotlib.pyplot as plt, numpy as np

from dream_agent import Agent

# from simulation import *
# from settings import *
# from event import *

class Statistics(Agent):

    def event_proc(self, id_event):
        if id_event == Event.start:
            self._file = open(Settings.out_file, "w") # Not used

            # Initialize graphics
            if Settings.graphics_show:
                plt.ion()
                plt.figure(figsize=[5,5])

        elif id_event == Event.stop:
            self._file.close()  # Not used

        elif id_event == Event.period_start:
            print(Simulation.time)

            if Settings.graphics_show:
                if Simulation.time % Settings.graphics_periods_per_pic==0:
                    # Gather data from population
                    w = []
                    for p in Simulation.population:
                        w.append(math.log(p.get_wealth()))

                    # Display data
                    plt.clf()
                    plt.hist(w, bins=50, color="blue")
                    plt.axis(ymin=0, ymax=100)
                    plt.title("Distribution of log-wealth ({})".format(Simulation.time))
                    plt.show()
                    plt.pause(0.000001)
