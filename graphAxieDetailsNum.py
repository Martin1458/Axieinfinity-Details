import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

appl = pd.read_csv("AxieDetails.csv")
##
ac = appl['id'].astype('str')
if type(ac)==int:
    print(' max   : ' + str(max(ac)))
    print(' min   : ' + str(min(ac)))
    print(' stdev : ' + str(np.std(ac)))
    print(' avg   : ' + str(np.mean(ac)))
    print(' median: ' + str(np.median(ac)))
else:
    #print(str(ac)+'are not numbers')
    pass

priceReasonable = str(appl['hp'])

plt.figure(figsize=(10,5))
plt.plot(str(appl['id']),str(appl['priceReasonable']),'k-',linewidth=3)
plt.xticks(rotation=90)
plt.legend(loc='best')
plt.show()