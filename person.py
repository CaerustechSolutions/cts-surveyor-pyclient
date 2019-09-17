import json

class Person:

    json = None
    rectangle = None
    id = None

    def __init__(self, person_json):
    
        self.json = person_json
        rect_json = person_json["rectangle"]
        x = rect_json["x"]
        y = rect_json["y"]
        endX = rect_json["endX"]
        endY = rect_json["endY"]
        self.rectangle = (x, y, endX, endY)
        self.id = person_json["id"]