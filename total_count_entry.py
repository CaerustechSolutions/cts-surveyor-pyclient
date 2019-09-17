import json

class TotalCountEntry:
    count = 0
    json = None

    def __init__(self, entry_json):
        self.json = entry_json
        self.count = entry_json["count"]