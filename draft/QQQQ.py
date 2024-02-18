from tkinter import Tk, Label, Entry, Button, filedialog
from models.URLMaker import URLMaker
from tools.Survey import SurveySubmitter
from tools.JSONReader import SurveyCSVReader
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

        self.browse_button = Button(root, text="Browse CSV", command=self.browse_csv)
        self.browse_button.pack()

        self.csv_status_label = Label(root, text="CSV not added", fg="red")
        self.csv_status_label.pack()

        self.submit_button = Button(root, text="Submit Survey", command=self.submit_survey)
        self.submit_button.pack()

        self.csv_file_path = ""




    def browse_csv(self):
        self.csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.csv_file_path:
            self.csv_status_label.config(text="CSV added", fg="green")

    def submit_survey(self):
        base_url = self.base_url_entry.get()
        entry_numbers = self.entries_entry.get().split(',')

        url_maker = URLMaker(base_url)
        survey_submitter = SurveySubmitter(url_maker)

        if not self.csv_file_path:
            print("Please select a CSV file.")
            return

        csv_reader = SurveyCSVReader(self.csv_file_path)
        survey_data = csv_reader.read_data_from_csv()

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










