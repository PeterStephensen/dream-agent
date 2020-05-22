from dream_agent import Agent
# from event import *
# from settings import *
# from person import *
#from statistics import *

class Simulation(Agent):
    # Static fields
    population = Agent()
    time = 0

    def __init__(self):
        super().__init__()
        # Initial allocation of all agents

        # Simulation has two children:
        self._statistics = Statistics(self)
        Simulation.population = Agent(self)

        # Adding persons to the population
        for i in range(Settings.number_of_agents):
            Person(Simulation.population)

        # Start the simulation
        self.event_proc(Event.start)

    def event_proc(self, id_event):
        if id_event == Event.start:
            # Send Event.start down the tree to all defendants
            super().event_proc(id_event)

            # The Event Pump: the actual simulation
            while Simulation.time < Settings.number_of_periods:
                # Important when agents are searching
                Simulation.population.randomize_agents()                #1
                self.event_proc(Event.period_start)
                self.event_proc(Event.update)
                Simulation.time += 1

            # Stop the simulation
            self.event_proc(Event.stop)

        else:
            # All other events are send to defendants
            super().event_proc(id_event)
