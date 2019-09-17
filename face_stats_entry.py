import json

class FaceStatsEntry:
    id = 0
    gender = 'unknown'
    age_lower = 0
    age_higher = 99
    detected_time = ''
    json = None

    def __init__(self, entry_json):
        self.json = entry_json
        self.id = entry_json["id"]
        self.gender = entry_json["gender"]
        self.age_lower = entry_json["age_lower"]
        self.age_higher = entry_json["age_higher"]
        self.detected_time = entry_json["detected_time"]