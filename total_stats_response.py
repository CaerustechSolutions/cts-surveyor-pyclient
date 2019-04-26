import json
from stats_count_entry import StatsCountEntry

class TotalStatsResponse:

    entry = None
    json = None
    
    def __init__(self, response_json):
    
        self.entries = []
        self.json = json.loads(response_json)
        self.entry = StatsCountEntry(self.json)
        