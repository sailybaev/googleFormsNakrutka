import csv
class SurveyCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def getHeaders(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return reader.fieldnames

    def read_data_from_csv(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader.fieldnames)
            return list(reader)
