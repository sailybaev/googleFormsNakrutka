import json

import google.generativeai as genai
class GenResponses:

    genai.configure(api_key="api from gemini")

    model = genai.GenerativeModel('gemini-pro')

    def genResp(self , query , path):

        response = self.model.generate_content(query)

        ss = response.text
        ss = ss.replace('\n', ' ').replace(' ' , '')

        with open(path , 'w') as f:
            f.write(ss)

        return ss