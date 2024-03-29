import random

class Agent:
    """Class used for agent based modelling and microsimulation
    """
    _nAgents = 0

    def __init__(self, parent=None):
        """Constructor for the Agent class

        Keyword Arguments:
            parent {Agent} -- The parent object (default: {None})
        """

        self._id = Agent._nAgents
        Agent._nAgents += 1
        self._first, self._next = None, None
        self._prev, self._last = None, None
        self._parent, self._a_itt = None, None
        self._count = 0
        self.removed, self.remove_when_empty = False, False
        self._random_agent=None
        
        if parent != None: parent.add_agent(self)

    def event_proc(self, id_event):
        """This method describes the behavior of the agent

        Arguments:
            id_event {Enum} -- An id that identifies the event that the agent experiences
        """
        for a in self:
            a.event_proc(id_event)
        
        if self.remove_when_empty and self._count==0:
            self.remove_this_agent()

    def add_agent(self, a):
        """Add new child agent

        Arguments:
            a {Agent} -- The new child agent
        """
        # Release old relations
        a.remove_this_agent()

        # Create new relations
        a._prev, a._next = self._last, None
        a._parent = self
    
        if self._first == None:
            self._first = a
        else:
            self._last._next = a

        self._last = a
        self._count += 1


    def remove_agent(self, a):
        """Remove a child agent

        Arguments:
            a {Agent} -- The child agent that should be removed
        """
        self.removed = True

        if self._count==1:
            self._first, self._last = None, None
        else:
            if a._prev != None: a._prev._next = a._next
            if a._next != None: a._next._prev = a._prev
            
            if a == self._first: self._first = a._next
            if a == self._last: self._last = a._prev

        self._count -= 1


    def remove_this_agent(self):
        """Removes this agent from it's connection to the parent agent. The agent ceases to exit.
        """
        if self._parent != None:
            self._parent.remove_agent(self)

    def randomize_agents(self):
        """The order of the child agents are randomized.
        """
        if self._count>1:
            lst = []
            for a in self: lst.append(a)
            random.shuffle(lst)
            self._first, self._last = lst[0], lst[-1]
            lst[0]._prev, lst[0]._next = None, lst[1]
            lst[-1]._prev, lst[-1]._next = lst[-2], None
            if self._count>2:
                for i in range(1,self._count-1):
                    lst[i]._prev, lst[i]._next = lst[i-1], lst[i+1]


    def get_random_agent(self, not_this_agent=None, n=1):
        """A random child agent is returned

        Keyword Arguments:
            not_this_agent {Agent} -- An agent not to return. Will often be 'this'.  (default: {None})
            n {int} -- Number of agents to return. If the number of agents is less than n, all agents are returned.  (default: {1})

        Returns:
            Agent -- A random agent. Returns None if no children
        """
        # If no children
        if self._first == None:
            return None

        if self._random_agent == None:
            self._random_agent = self._first

        nn = n  #0.3
        if n > self._count:
            nn = self._count

        ls = []
        i = 0

        while (i < nn):
            if self._random_agent != not_this_agent or not_this_agent==None:
                ls.append(self._random_agent)
                i += 1
            if self._random_agent._next != None:
                self._random_agent = self._random_agent._next
            else:
                self._random_agent = self._first

        if nn == 1:
            return ls[0]
        else:
            return ls


    # Initialize iterator
    def __iter__(self):
        self._a_itt = self._first
        return self

    # Iterate iterator
    def __next__(self):
        if self._a_itt is not None:
            a = self._a_itt
            self._a_itt = self._a_itt._next
            return a
        else:    
            raise StopIteration

    def __eq__(self, other):
        return self._id==other

    def __ne__(self, other):
        return self._id!=other

    def __len__(self):
        if self._first==None:
            return 0
        else:
            return self._count

    def count(self):
        """Get the number of children

        Returns:
            int -- The number of children
        """
        return self._count

    def get_number_of_agents(self):
        """Get the number of children

        Returns:
            int -- The number of children
        """
        return self._count

    def number_of_agents(self):
        """Get the number of children

        Returns:
            int -- The number of children
        """
        return self._count

    def get_id(self):
        """Get the agents unique ID

        Returns:
            int -- Unique agent ID
        """
        return self._id

    @staticmethod
    def get_total_number_of_agents():
        """Get total number of agents in the current simulation

        Returns:
            int -- The total number of agents in the current simulation
        """
        return Agent._nAgents

