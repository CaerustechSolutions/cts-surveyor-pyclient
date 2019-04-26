import json

class Person:

    json = None
    rectangle = None
    gender = None
    age = None
    id = None

    def __init__(self, person_json):
    
        self.json = person_json
        rect_json = person_json["rectangle"]
        x = rect_json["x"]
        y = rect_json["y"]
        w = rect_json["width"]
        h = rect_json["height"]
        self.rectangle = (x, y, w, h)
        self.gender = person_json["gender"]
        self.age = person_json["age"]
        self.id = person_json["id"]