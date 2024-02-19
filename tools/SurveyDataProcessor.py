import re

class SurveyDataProcessor:
    def __init__(self, survey_submitter):
        self.survey_submitter = survey_submitter

    def process_data(self, data, entry_numbers):
        if not data:
            print("No data to process.")
            return

        for row in data:
            form_data = {f'entry.{entry_num.strip()}': str(value) for entry_num, value in zip(entry_numbers, row.values())}
            self.survey_submitter.submit_response(form_data)
            print('\033[36m'"Submitted:", row)


