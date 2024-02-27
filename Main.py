from tkinter import Tk, Label, Entry, Button, Menu, filedialog, Toplevel, Text
import json
from models.URLMaker import URLMaker
from tools.Survey import SurveySubmitter
from tools.FileReader import SurveyFileReader
from tools.SurveyDataProcessor import SurveyDataProcessor
from tools.QrGenRead import QRScanner
from AI import GenResponses
from AI import TextProcessor

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

        self.generate_ai_label = Label(root, text="AI Generate:")
        self.generate_ai_label.pack()

        self.num_responses_label = Label(root, text="Number of Responses (3-6):")
        self.num_responses_label.pack()

        self.num_responses_entry = Entry(root)
        self.num_responses_entry.pack()

        self.details_label = Label(root, text="Details of Questions:")
        self.details_label.pack()

        self.details_entry = Entry(root)
        self.details_entry.pack()

        self.generate_ai_button = Button(root, text="Generate AI Text", command=self.generate_ai_text)
        self.generate_ai_button.pack()

        self.generated_ai_text_label = Label(root, text="Generated AI Text:")
        self.generated_ai_text_label.pack()

        self.generated_ai_text = Text(root, height=5, width=40)
        self.generated_ai_text.pack()

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

            with open("tempFiles/entries_and_link.json", "w") as entries_file:
                json.dump(entries_and_link, entries_file, indent=2)

            with open("tempFiles/user_info.json", "w") as user_info_file:
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

    def generate_ai_text(self):
        num_responses = int(self.num_responses_entry.get())
        details_of_questions = self.details_entry.get()

        with open('AI/user_input.txt' , 'w') as f:
            f.write(details_of_questions)

        gen = GenResponses.GenResponses()
        tt = TextProcessor.TextProcessor()
        query = tt.get_input("AI/user_input.txt", num_responses)

        generated_text = gen.genResp(query, 'tempFiles/aiGeneratedJson.json')

        # Update the Text widget with the generated text.
        self.generated_ai_text.delete(1.0, 'end')  # Clear existing text
        self.generated_ai_text.insert('end', "Json is generated, now you can\nchoose it in json selector\nfile name: aiGeneratedJson.json")

if __name__ == "__main__":
    root = Tk()
    app = SurveyApp(root)
    root.mainloop()
