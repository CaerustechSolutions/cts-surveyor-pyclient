import json

class Face:

    json = None
    gender = None
    ageLower = None
    ageUpper = None

    def __init__(self, face_json):
    
        self.json = face_json
        self.gender = face_json["gender"]
        self.ageLower = face_json["ageLower"]
        self.ageUpper = face_json["ageUpper"]