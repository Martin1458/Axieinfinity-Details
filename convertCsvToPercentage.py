import pandas as pd
import numpy as np
import csv

def percentage(part, whole):
  if part != 0:
    return 100 * float(part)/float(whole)
  else:
    return float(0)

pathToNewCsv = "SmallAxieDetailsPercentage.csv"
axieCsv = pd.read_csv("AxieSmallDetails.csv")
axieCsvHeaders = list(axieCsv.columns)
percentageAxieCsv = []
ids = []
print(axieCsv['id'])
for id in axieCsv['id']:
  ids.append(id)

print(axieCsv)
percentageAxieCsv.append(ids)
for item in axieCsvHeaders:
    if item != 'id':
        currArray = []
        maxOfItem = max(axieCsv[item])
        for value in axieCsv[item]:
          currArray.append(percentage(value, maxOfItem))
        percentageAxieCsv.append(currArray)

print(percentageAxieCsv)

dataToWrite = zip(*percentageAxieCsv)

open(pathToNewCsv, 'w').close()

with open(pathToNewCsv, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(axieCsvHeaders)
  writer.writerows(dataToWrite)
