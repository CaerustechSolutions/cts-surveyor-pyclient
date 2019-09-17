import json

class StatsCountEntry:

    start = ''
    end = ''
    count = 0
    json = None
    
    def __init__(self, entry_json):
    
        self.json = entry_json
        self.start = entry_json["start"]
        self.end = entry_json["end"]
        self.count = entry_json["count"]