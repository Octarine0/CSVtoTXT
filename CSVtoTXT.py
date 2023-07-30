import pandas as pd
import json
from os import listdir

#loading options
try:
    optionsFile = open("Options.json")
    options = json.load(optionsFile)
except:
    #print("hi")
    options = {
        "inputFolder": "Input/",
        "outputFolder": "Output/",
        "verbose": True,
        "Column": 1,
        "Rows": 0
    }
    with open("Options.json", "w") as optionsOut:
        json.dump(options, optionsOut, indent = 1) #indent for clarity


inputs = listdir(options["inputFolder"])
if (inputs.count == 0):
    print("No inputs found, program ending.")
    exit()

fileCount = 0
for fileName in inputs:
    fileCount += 1
    try:
        filePath = options["inputFolder"] + fileName
        columnFrame = pd.read_csv(filePath, usecols=[options["Column"]])
        
    except:
        print("Could not open file at: " + filePath)
        break

    #columnFrame = rawDataFrame.usecols=[options["Column"]]
    if (options["Rows"] <= 0):
        rowsToConvert = len(columnFrame)
    for i in range(rowsToConvert):
        data = columnFrame.iloc[[i]]
        outputFile = open(options["outputFolder"] + "File" + str(fileCount) + "Row" +  str(i) + ".txt", "w")
        outputFile.write(data.to_string(header=False, index=False))
        outputFile.close()
print ("Transfer Complete")