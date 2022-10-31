import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

axieCsv = pd.read_csv("AxieSmallDetails.csv")
axieCsvHeaders = list(axieCsv.columns)
graphColors = ['--b', '--g', '--r', '--c', '--m', '--y', '--k', '--w' , ':b', ':g', ':r', ':c']

print(len(axieCsvHeaders))
print(len(graphColors))

plt.figure(figsize=(20,10))

for item in axieCsvHeaders:
    ac = axieCsv[item]
    print(' {} - max   : {}'.format(item, str(max(ac))))
    print(' {} - min   : {}'.format(item, str(min(ac))))
    print(' {} - stdev : {}'.format(item, str(np.std(ac))))
    print(' {} - avg   : {}'.format(item, str(np.mean(ac))))
    print(' {} - median: {}'.format(item, str(np.median(ac))))
    print("\n\n")

    if item != 'id':
        plt.plot(axieCsv['id'],axieCsv[item], graphColors[axieCsvHeaders.index(item)-1], linewidth=1, label=item)

#plt.xticks(rotation=90)
plt.xlabel("Axie id")
plt.legend()
plt.show()
