# creating  a json database

import json

link_to_json = "./json_test.json"

with open("./json_test.json", mode="r") as file:
    json_file = json.load(file)
    print(json_file["Alice"])
