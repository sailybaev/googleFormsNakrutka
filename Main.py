from tkinter import Tk, Label, Entry, Button, filedialog
from models.URLMaker import URLMaker
from tools.Survey import SurveySubmitter
from tools.JSONReader import SurveyJSONReader
from tools.SurveyDataProcessor import SurveyDataProcessor

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Data Submission")

        self.base_url_label = Label(root, text="Enter Google Forms URL:")
        self.base_url_label.pack()

        self.base_url_entry = Entry(root)
        self.base_url_entry.pack()

        self.entries_label = Label(root, text="Enter entry numbers (comma-separated):")
        self.entries_label.pack()

        self.entries_entry = Entry(root)
        self.entries_entry.pack()

        self.browse_button = Button(root, text="Browse JSON", command=self.browse_json)
        self.browse_button.pack()

        self.json_status_label = Label(root, text="JSON not added", fg="red")
        self.json_status_label.pack()

        self.submit_button = Button(root, text="Submit Survey", command=self.submit_survey)
        self.submit_button.pack()

        self.json_file_path = ""




    def browse_json(self):
        self.json_file_path = filedialog.askopenfilename(filetypes=[("json Files", "*.json")])
        if self.json_file_path:
            self.json_status_label.config(text="JSON added", fg="green")

    def submit_survey(self):
        base_url = self.base_url_entry.get()
        entry_numbers = self.entries_entry.get().split(',')

        url_maker = URLMaker(base_url)
        survey_submitter = SurveySubmitter(url_maker)

        if not self.json_file_path:
            print("Please select a JSON file.")
            return

        json_reader = SurveyJSONReader(self.json_file_path)
        survey_data = json_reader.read_data_from_json()

        data_processor = SurveyDataProcessor(survey_submitter)
        data_processor.process_data(survey_data, entry_numbers)


if __name__ == "__main__":
    root = Tk()
    app = SurveyApp(root)
    root.mainloop()


#https://docs.google.com/forms/d/e/1FAIpQLSeObLLkxB5g5Hfo7nhvPm7rfx1BEjdI-pb_ydT6HkYysYRq9Q
#/Users/sailybaev/PycharmProjects/pythonProject2/db.csv
# 1194903177,1642021955,157922501,123662009,762022727
# 397594751
# 1135559429,2114464800,1352402628,509642671,34648482,972909645,1405518975,750277378,1995628285,546101484
# https://docs.google.com/forms/d/e/1FAIpQLScCB1m35Et28Ylx98ry5vxVQhxFudq5_eCbHGQdybAiEd2L-g









