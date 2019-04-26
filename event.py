import json
from person import Person

class Event:
    
    event_type = None
    json = None
    people = []
    
    def __init__(self, event_json):
    
        self.json = event_json        
        self.event_type = event_json["event"]
        if event_json.get("people"):
            people_json = event_json["people"]
            i = 0
            while i < len(people_json):
                person_json = people_json[i]
                person = Person(person_json)
                self.people.append(person)
                i += 1