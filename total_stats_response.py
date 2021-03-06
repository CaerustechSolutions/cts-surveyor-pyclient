import json
from total_count_entry import TotalCountEntry

class TotalStatsResponse:

    entry = None
    json = None
    
    def __init__(self, response_json):
    
        self.entries = []
        self.json = json.loads(response_json)
        self.entry = TotalCountEntry(self.json)
        