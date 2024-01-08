import requests
import csv

def submit_survey_response(a, b, c, d, e):
    GoogleURL = 'tvoi Url'

    urlResponse = GoogleURL + '/formResponse'
    urlReferer = GoogleURL + '/viewform'

    form_data = {
        'entry.1194903177': a,  # Convert back to string for submission
        'entry.1642021955': b,
        'entry.157922501': c,
        'entry.123662009': d,
        'entry.762022727': e
    }

    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

    try:
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

file_path = '/Users/sailybaev/PycharmProjects/pythonProject/db.csv'
read_survey_data_from_csv(file_path)
