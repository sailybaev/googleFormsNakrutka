from URLMaker import URLMaker
from Survey import SurveySubmitter
from CSVReader import SurveyCSVReader
from SurveyDataProcessor import SurveyDataProcessor
import colorama

def get_base_url():
    return input("Enert google forms URL: ")
    #return 'https://docs.google.com/forms/d/e/1FAIpQLSeObLLkxB5g5Hfo7nhvPm7rfx1BEjdI-pb_ydT6HkYysYRq9Q'
def get_csv_file_path():
    return input("Enter path to the CSV file: ")
    #return '/Users/sailybaev/PycharmProjects/pythonProject2/db.csv'

def main():
    base_url = get_base_url()
    url_maker = URLMaker(base_url)
    survey_submitter = SurveySubmitter(url_maker)

    csv_file_path = get_csv_file_path()
    csv_reader = SurveyCSVReader(csv_file_path)
    survey_data = csv_reader.read_data_from_csv()

    data_processor = SurveyDataProcessor(survey_submitter)
    data_processor.process_data(survey_data)

if __name__ == "__main__":
    main()

#https://docs.google.com/forms/d/e/1FAIpQLSeObLLkxB5g5Hfo7nhvPm7rfx1BEjdI-pb_ydT6HkYysYRq9Q
#/Users/sailybaev/PycharmProjects/pythonProject2/db.csv
# 1194903177,1642021955,157922501,123662009,762022727
# 397594751










