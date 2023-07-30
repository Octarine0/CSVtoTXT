import csv
import json

#loading options
try:
    options_file = open("Options.json")
    options = json.load(options_file)
except:
    #print("hi")
    options = {
        "inputFolder": "Input/",
        "outputFolder": "Output/",
        "Column": 1,
        "Rows": 0
    }
    with open("Options.json", "w") as optionsOut:
        json.dump(options, optionsOut, indent = 1) #indent for clarity

