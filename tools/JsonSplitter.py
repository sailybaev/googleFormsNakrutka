import json
class JsonSplitter:
    # Read JSON data from file
    with open("input_data.json", "r") as file:
        json_data = json.load(file)

    entries_and_link = json_data[0]
    user_info = json_data[1]

    with open("entries_and_link.json", "w") as entries_file:
        json.dump(entries_and_link, entries_file, indent=2)

    with open("user_info.json", "w") as user_info_file:
        json.dump(user_info, user_info_file, indent=2)

    print("Files saved successfully.")
