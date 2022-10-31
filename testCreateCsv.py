import csv
import random

header = ["id", "hp", "price"]
data = [
    
]

def writeData(nameOfFile, headerRow, dataRows):
    with open(nameOfFile, 'w') as f:
        writer = csv.writer(f)

        writer.writerow(headerRow)
        writer.writerows(dataRows)


def getNewRow(id):
    hp = random.randint(27, 61)
    return [id, hp, random.randint(1, 100)*hp]

if __name__ == '__main__':
    print("Data:", data)
    for i in range(50000):
        data.append(getNewRow(i+1))
        #print("Data:", data)
    writeData("testWrite.csv", header, data)
    