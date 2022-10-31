import pandas as pd
import csv
from math import floor

pathToCsv = '~/Desktop/pythonShit/AxieInfinity/AxieDetails.csv'
pathToNewCsv ='/home/martin/Desktop/pythonShit/AxieInfinity/AxieSmallDetails100.csv'

axieCsv = pd.read_csv(pathToCsv)
axieCsvHeaders = list(axieCsv.columns)
newData = []
newDataRows = []
counter = float(0)
whatToConvert = list(['id', 'level', 'hp', 'skill', 'speed', 'morale', 'breedCount', 'stage', 'priceLast', 'priceQuick', 'priceReasonable', 'pricePatient', 'similarAxies'])
# How many times to compress
compress = 100
h = 0
csvRows = len(axieCsv.index) // 100
csvRowsLeft = len(axieCsv.index) - (csvRows * 100)
axieCsv.fillna(0, inplace = True)


for e in range(len(whatToConvert)):
    newData.append([])

for i in range(1):
    for item in whatToConvert:
        print(item)
        for e in range(csvRows):
            if (compress*e)+compress > (csvRows*100):
                z = (compress*e)+csvRowsLeft
            else:
                z = (compress*e)+compress
            for k in range(compress*e, z):
                if axieCsv[item][k] != 'nan':
                    try:
                        counter += float(axieCsv[item][k])
                    except:
                        counter += float(0)
                        pass
                    if item == 'id':
                        #print(axieCsv[item][k])
                        pass
            #print(counter)
            newData[h].append(counter/compress)
            counter = float(0)
        h += 1

priceQuickV = 'priceQuick'
print("\n\n")
print(axieCsv[priceQuickV][11])
print(axieCsv[priceQuickV][11] == "nan")
print(axieCsv[priceQuickV][11] == "")
print(axieCsv[priceQuickV][11] == None)
#print(axieCsv[priceQuickV][11] == Null)
#convert newData to rows
for i in range(len(newData[0])):
    newDataRows.append([])

for i in range(len(newData[0])):
    for e in range(len(whatToConvert)):
        newDataRows[i].append(newData[e])

def writeIt():
    newRow = []
    with open(pathToNewCsv, 'w') as f:
            writer = csv.writer(f)

            writer.writerow(whatToConvert)
            for i in range(len(newData[0])):
                for e in range(len(newData)):
                    newRow.append(newData[e][i])
                writer.writerow(newRow)
                newRow = []
                
def deleteIt():
    open('AxieSmallDetails100.csv', 'w').close()

print("\n\n\n\n\n")
#for r in range(len(newDataRows)):
#    print(newDataRows[r])
print(newDataRows[0][0])

deleteIt()
writeIt()
