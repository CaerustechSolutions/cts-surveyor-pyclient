import json

class StatsEntry:

    id = 0
    arrived = ''
    left = ''
    json = None
    
    def __init__(self, entry_json):
    
        self.json = entry_json
        self.id = entry_json["id"]
        self.arrived = entry_json["arrived"]
        self.left = entry_json["left"]