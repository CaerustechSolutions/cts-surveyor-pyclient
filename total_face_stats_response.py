import json
from total_face_count_entry import TotalFaceCountEntry

class TotalFaceStatsResponse:
    entry = None
    json = None

    def __init__(self, response_json):
        self.entries = []
        self.json = json.loads(response_json)
        self.entry = TotalFaceCountEntry(self.json)
