class Event:
    def __init__(self, time, event_type, target):
        self.time = time
        self.event_type = event_type  # e.g. FAIL_NODE
        self.target = target


class Scenario:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, time, event_type, target):
        self.events.append(Event(time, event_type, target))

    def get_events_at_time(self, time):
        return [e for e in self.events if e.time == time]
