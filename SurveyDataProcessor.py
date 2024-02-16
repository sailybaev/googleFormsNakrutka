class SurveyDataProcessor:
    def __init__(self, survey_submitter):
        self.survey_submitter = survey_submitter

    def process_data(self, data):
        if not data:
            print("No data to process.")
            return

        entry_numbers = input("Enter entry numbers separated by commas (e.g., 123,456): ").split(',')

        for row in data:
            form_data = {f'entry.{entry_num.strip()}': str(value) for entry_num, value in zip(entry_numbers, row.values())}
            self.survey_submitter.submit_response(form_data)
            print('\033[36m'+"Submitted:", row)
