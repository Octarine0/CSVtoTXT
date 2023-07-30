import pandas as pd
import json
from os import listdir
import re

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
        "tidyData": True,
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
        columnFrame = pd.read_csv(filePath, usecols=[options["Column"] - 1])
        
    except:
        print("Could not open file at: " + filePath)
        break

    #columnFrame = rawDataFrame.usecols=[options["Column"]]
    if (options["Rows"] <= 0):
        rowsToConvert = len(columnFrame)
    else:
        rowsToConvert = options["Rows"]
    for i in range(rowsToConvert):
        data = columnFrame.iloc[[i]]
        stringData = data.to_string(header=False, index=False)
        if (options["tidyData"]): 
            stringData = stringData.strip()
            stringData = re.sub('\s{2,}', ' ', stringData)
        outputFile = open(options["outputFolder"] + "File" + str(fileCount) + "Row" +  str(i) + ".txt", "w", encoding="utf-8")
        outputFile.write(stringData)
        outputFile.close()
        if options["verbose"] and rowsToConvert >= 4:
            if i == rowsToConvert:
                print("100% complete")
            elif i == int((rowsToConvert*0.75)):
                print("75% complete")
            elif i == int((rowsToConvert*0.5)):
                print("50% complete")
            elif i == int((rowsToConvert*0.25)):
                print("25% complete")

            if rowsToConvert >= 20:
                if i == int((rowsToConvert*0.1)):
                    print("10% complete")
                elif i == int((rowsToConvert*0.2)):
                    print("20% complete")
                elif i == int((rowsToConvert*0.3)):
                    print("30% complete")
                elif i == int((rowsToConvert*0.4)):
                    print("40% complete")
                elif i == int((rowsToConvert*0.6)):
                    print("60% complete")
                elif i == int((rowsToConvert*0.7)):
                    print("70% complete")
                elif i == int((rowsToConvert*0.8)):
                    print("80% complete")
                elif i == int((rowsToConvert*0.9)):
                    print("90% complete")
print ("Transfer Complete")