from tkinter import Tk, Label, Entry, Button, Menu, filedialog, Toplevel
import json
from models.URLMaker import URLMaker
from tools.Survey import SurveySubmitter
from tools.FileReader import SurveyFileReader
from tools.SurveyDataProcessor import SurveyDataProcessor
from tools.QrGenRead import QRScanner

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Data Submission")

        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open JSON File", command=self.browse_json)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

        self.base_url_label = Label(root, text="Enter Google Forms URL:")
        self.base_url_label.pack()

        self.base_url_entry = Entry(root)
        self.base_url_entry.pack()

        self.entries_label = Label(root, text="Enter entry numbers (comma-separated):")
        self.entries_label.pack()

        self.entries_entry = Entry(root)
        self.entries_entry.pack()

        self.scan_qr_button = Button(root, text="Scan QR Code", command=self.open_qr_scanner)
        self.scan_qr_button.pack()

        self.add_json_button = Button(root, text="Add JSON", command=self.browse_json)
        self.add_json_button.pack()

        self.json_status_label = Label(root, text="JSON not added", fg="red")
        self.json_status_label.pack()

        self.submit_button = Button(root, text="Submit Survey", command=self.submit_survey)
        self.submit_button.pack()

        self.json_file_path = ""

    def browse_json(self):
        self.json_file_path = filedialog.askopenfilename(filetypes=[("json Files", "*.json")])
        if self.json_file_path:
            self.json_status_label.config(text="JSON added", fg="green")

    def open_qr_scanner(self):
        qr_scanner_window = Toplevel(self.root)
        qr_scanner_window.title("QR Code Scanner")
        qr_scanner = QRScanner(qr_scanner_window, self.update_qr_data)

    def update_qr_data(self, qr_data):
        qr_parts = json.loads(qr_data)

        if len(qr_parts) == 2:
            entries_and_link, user_info = qr_parts

            with open("/Users/sailybaev/PycharmProjects/googleFormsNakrutka/tempFiles/entries_and_link.json", "w") as entries_file:
                json.dump(entries_and_link, entries_file, indent=2)

            with open("/Users/sailybaev/PycharmProjects/googleFormsNakrutka/tempFiles/user_info.json", "w") as user_info_file:
                json.dump(user_info, user_info_file, indent=2)

            self.base_url_entry.delete(0, 'end')
            self.base_url_entry.insert(0, entries_and_link.get("link", ""))
            self.entries_entry.delete(0, 'end')
            self.entries_entry.insert(0, entries_and_link.get("entries", ""))
            self.json_status_label.config(text="QR Code scanned and processed", fg="green")
            self.json_file_path = 'user_info.json'

    def submit_survey(self):
        base_url = self.base_url_entry.get()
        entry_numbers = self.entries_entry.get().split(',')

        url_maker = URLMaker(base_url)
        survey_submitter = SurveySubmitter(url_maker)

        if not self.json_file_path:
            print("Please select a JSON file.")
            return

        json_reader = SurveyFileReader(self.json_file_path)
        survey_data = json_reader.read_data_from_json()

        print("Type of survey_data:", type(survey_data))
        print("Content of survey_data:", survey_data)

        data_processor = SurveyDataProcessor(survey_submitter)
        data_processor.process_data(survey_data, entry_numbers)

    def process_survey_information(self, survey_info):
        entry_numbers = survey_info.get("entries", "").split(',')
        google_forms_link = survey_info.get("link", "")

        self.entries_entry.delete(0, 'end')
        self.entries_entry.insert(0, ','.join(entry_numbers))
        self.base_url_entry.delete(0, 'end')
        self.base_url_entry.insert(0, google_forms_link)
        self.json_status_label.config(text="Survey information processed", fg="green")

    def process_survey_responses(self, survey_responses):
        base_url = self.base_url_entry.get()
        entry_numbers = self.entries_entry.get().split(',')

        if not base_url or not entry_numbers:
            print("Please enter a Google Forms URL or scan a QR code.")
            return

        url_maker = URLMaker(base_url)
        survey_submitter = SurveySubmitter(url_maker)

        survey_data = survey_responses[0]

        data_processor = SurveyDataProcessor(survey_submitter)
        data_processor.process_data(survey_data, entry_numbers)

if __name__ == "__main__":
    root = Tk()
    app = SurveyApp(root)
    root.mainloop()
