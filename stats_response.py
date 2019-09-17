import json
from stats_entry import StatsEntry

class StatsResponse:

    entries = []
    json = None
    
    def __init__(self, response_json):
    
        self.entries = []
        self.json = json.loads(response_json)
        i = 0
        while i < len(self.json):
            entry = StatsEntry(self.json[i])
            self.entries.append(entry)
            i += 1