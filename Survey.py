# survey_submitter.py
import requests

class SurveySubmitter:
    def __init__(self, url_maker):
        self.url_maker = url_maker

    def submit_response(self, form_data):
        url_response = self.url_maker.form_response_url()
        url_referer = self.url_maker.view_form_url()

        user_agent = {'Referer': url_referer,
                      'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

        try:
            print("fromd-", form_data)
            r = requests.post(url_response, data=form_data, headers=user_agent)
            r.raise_for_status()
            print('\033[32m'+"Kaif! Tebe povezlo")
        except requests.RequestException as e:
            print('\033[31m'+"Chort ekensn:", e)