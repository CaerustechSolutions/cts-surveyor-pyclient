import json
from face_stats_entry import FaceStatsEntry

class FaceStatsResponse:
    entries = []
    json = None

    def __init__(self, response_json):
        self.entries = []
        self.json = json.loads(response_json)
        i = 0
        while i < len(self.json):
            entry = FaceStatsEntry(self.json[i])
            self.entries.append(entry)
            i += 1