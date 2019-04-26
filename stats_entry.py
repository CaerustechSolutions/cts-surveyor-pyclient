import json

class StatsEntry:

    id = 0
    age_lower = 0
    age_upper = 99
    gender = 'U'
    arrived = ''
    json = None
    
    def __init__(self, entry_json):
    
        self.json = entry_json
        self.id = entry_json["id"]
        self.age_lower = entry_json["age_lower"]
        self.age_upper = entry_json["age_higher"]
        self.gender = entry_json["gender"]
        self.arrived = entry_json["arrived"]