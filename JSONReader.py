import json

class SurveyJSONReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data_from_json(self):
        with open(self.file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
        return data