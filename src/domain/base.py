#a base class is a class that other classes can inherit from
#Aggregate root is a base class BusTrip inherits from it 
#event collection behavior for aggregate roots


class AggregateRoot:  #parent class for aggregate roots
    

    def __init__(self):   #every aggregate starts with an empty list of domain events
        self._events = []

    def _record(self, event):   #when something happens store the events
        self._events.append(event)

    def pull_events(self):
        events, self._events = self._events, []
        return events