from enum import Enum 

class Event(Enum):
    start = 1         # The model starts
    stop = 2          # The model stops
    period_start = 3  # The start of a period
    update = 4        # Stuff that happens in the period
