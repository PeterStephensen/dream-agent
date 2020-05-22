from dream_agent import Agent
# import random
# from event import *
# from settings import *
# from ecommunication import *

class Person(Agent):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._wealth = 1                                        #1
        self._strength = random.gauss(0,1)

    def event_proc(self, id_event):
        if id_event == Event.update:
            if random.random() < Settings.attack_probability:   #2
                # Random search
                p = Simulation.population.get_random_agent(self)
                # Communication
                if (p.communicate(ECommunication.I_attack, self) == ECommunication.you_lose):
                    self.transfer_to(p, Settings.loot_share * self._wealth)

    def communicate(self, ecommunicate, person):                #3
        if ecommunicate == ECommunication.I_attack:
            if self._strength < person._strength:
                self.transfer_to(person, Settings.loot_share * self._wealth)
                return ECommunication.you_win
            else:
                return ECommunication.you_lose

    def transfer_to(self, other, value):                       #4
        self._wealth -= value
        other._wealth += value

    def get_wealth(self):
        return self._wealth

