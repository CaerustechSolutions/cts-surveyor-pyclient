import json
from person import Person
from face import Face

class Event:
    
    event_type = None
    json = None
    people = []
    faces = []
    
    def __init__(self, event_json):
    
        self.people = []
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
        self.faces = []
        if event_json.get("faces"):
            faces_json = event_json["faces"]
            i = 0
            while i < len(faces_json):
                face_json = faces_json[i]
                face = Face(face_json)
                self.faces.append(face)
                i += 1                