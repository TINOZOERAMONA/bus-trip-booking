class AggregateRoot:
    """Layer Supertype: shared behaviour for aggregate roots.
    It only collects domain events so the application layer can publish them."""

    def __init__(self):
        self._events = []

    def _record(self, event):
        self._events.append(event)

    def pull_events(self):
        events, self._events = self._events, []
        return events