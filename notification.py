import json
from event import Event

class Notification:

    events = []
    json = None

    def __init__(self, notification_json):
    
        self.events = []
        events_json = json.loads(notification_json)
        self.json = events_json["events"]
        i = 0
        while i < len(self.json):
            event = Event(self.json[i])
            self.events.append(event)
            i += 1