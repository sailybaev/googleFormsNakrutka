import requests
import csv

def submit_survey_response(a, b, c, d, e):
    GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSeObLLkxB5g5Hfo7nhvPm7rfx1BEjdI-pb_ydT6HkYysYRq9Q'

    urlResponse = GoogleURL + '/formResponse'
    urlReferer = GoogleURL + '/viewform'

    form_data = {
        'entry.1194903177': a,
        'entry.1642021955': b,
        'entry.157922501': c,
        'entry.123662009': d,
        'entry.762022727': e
    }

    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

    try:
        print("fromd-",form_data)
        r = requests.post(urlResponse, data=form_data, headers=user_agent)
        r.raise_for_status()
        print("Kaif! tebe povezlo")
    except requests.RequestException as e:
        print("Chort ekensn: ", e)

def read_survey_data_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        for row in reader:

            submit_survey_response(
                row['a'],
                row['b'],
                row['c'],
                row['d'],
                row['e']
            )
            print("Submitted:", row)

file_path = '/Users/sailybaev/PycharmProjects/pythonProject2/db.csv'
read_survey_data_from_csv(file_path)

#Submitted: {'a': '4', 'b': 'Yes', 'c': 'Yes', 'd': 'Encourage intercultural events and festivals', 'e': 'Yes'}
#Submitted: {'a': '4', 'b': 'Yes', 'c': 'Yes', 'd': 'Encourage intercultural events and festivals', 'e': 'Yes'}


#fromd- {'entry.1194903177': 'a', 'entry.1642021955': 'b', 'entry.157922501': 'c', 'entry.123662009': 'd', 'entry.762022727': 'e'}
