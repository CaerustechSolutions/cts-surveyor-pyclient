import json

class FaceStatsCountEntry:
    start = ''
    end = ''
    male_count = 0
    female_count = 0
    child_teen_count = 0
    young_adult_count = 0
    adult_count = 0
    middle_aged_count = 0
    senior_count = 0
    json = None

    def __init__(self, entry_json):
        self.json = entry_json
        self.start = entry_json["start"]
        self.end = entry_json["end"]
        self.male_count = entry_json["male_count"]
        self.female_count = entry_json["female_count"]
        self.child_teen_count = entry_json["child_teen_count"]
        self.young_adult_count = entry_json["young_adult_count"]
        self.adult_count = entry_json["adult_count"]
        self.middle_aged_count = entry_json["middle_aged_count"]
        self.senior_count = entry_json["senior_count"]