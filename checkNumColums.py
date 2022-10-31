import pandas as pd

pathToCsv = '~/Desktop/pythonShit/AxieInfinity/AxieDetails.csv'

axieCsv = pd.read_csv(pathToCsv)
axieCsvHeaders = list(axieCsv.columns)

#print(axieCsvHeaders)
def printHeader():
    for head in axieCsvHeaders:
        print("{} on first line is {}".format(str(head), str(axieCsv[head][0])))
def checkIfNum(xxx):
    doesHeadMatch = False
    areAllNum = True
    allWrongCells = list([])
    allWrongCellsIndex = list([])
    for head in axieCsvHeaders:
        if(head == xxx):
            doesHeadMatch = True
            iii = 0
            for item in axieCsv[head]:
                if type(item) == int or type(item) == float or item == '':
                    #Is Number
                    #print(iii)
                    pass
                else:
                    areAllNum = False
                    currentWrongCell = axieCsv[head][iii]
                    allWrongCells.append(currentWrongCell)
                    allWrongCellsIndex.append(iii)
                iii += 1

    if not doesHeadMatch:
        print(xxx+' - Does not match any CSV header.')
    elif not areAllNum:
        print('Not all cells in {} are numbers.'.format(xxx))
        print("All cells, that are not numbers:")
        for i in range(len(allWrongCells)):
            #print(i)
            #print('{} at index {}'.format(allWrongCells[i], allWrongCellsIndex[i]))
            pass
    else:
        print('All cells in {} are numbers or empty.'.format(xxx))

def fromUserInput():
    return list(input('What column would you like to test: '))

def fromAllColums():
    return list(['id', 'level', 'hp', 'skill', 'speed', 'morale', 'breedCount', 'stage', 'priceLast', 'priceQuick', 'priceReasonable', 'pricePatient', 'similarAxies'])


for item in fromAllColums():
    checkIfNum(item)
    pass

printable = int(axieCsv.level[4])
print(printable)
print(type(printable))

