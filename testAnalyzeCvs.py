import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

appl = pd.read_csv("AAPL.csv")

ac = appl['Open']
print(' max   : ' + str(max(ac)))
print(' min   : ' + str(min(ac)))
print(' stdev : ' + str(np.std(ac)))
print(' avg   : ' + str(np.mean(ac)))
print(' median: ' + str(np.median(ac)))

plt.figure(figsize=(10,5))
plt.plot(appl['Date'],appl['Open'],'k-',linewidth=3)
plt.plot(appl['Date'],appl['High'],'r--',linewidth=1)
plt.plot(appl['Date'],appl['Low'],'b:',linewidth=1)
plt.xticks(rotation=90)
plt.legend(loc='best')
plt.show()