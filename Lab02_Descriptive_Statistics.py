import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

print("-----------------------------------------------")
print("August 2018 Nationwide Airplane Delay Statistic")
print("-----------------------------------------------")
print(sample_data.describe())
print("-----------------------------------------------\nMode\n-----------------------------------------------")
print(sample_data.mode())
print("-----------------------------------------------\nMeasures of spread (Dispersion)\n-----------------------------------------------")
print(str(max(sample_data.DEP_DELAY) - min(sample_data.DEP_DELAY)) + " (HHMM)")
print("-----------------------------------------------\nSimple Variance\n-----------------------------------------------")
print("DEP_DELAY : " + str(sample_data.DEP_DELAY.var()))
print("ARR_DELAY : " + str(sample_data.ARR_DELAY.var()))


plt.vlines(sample_data.DEP_DELAY.mean(),
           ymin=-90, 
           ymax=1070,
           linewidth=2.0,
           label='Mean of DEP_DELAY = {:+.2f}'.format(sample_data.DEP_DELAY.mean()));
plt.vlines(sample_data.DEP_DELAY.median(),
           ymin=-90, 
           ymax=1070, 
           linewidth=2.0,
           color="red",
           label='Median of DEP_DELAY = {:+.2f}'.format(sample_data.DEP_DELAY.median()));
plt.vlines(sample_data.DEP_DELAY.mode()[0],
           ymin=-90, 
           ymax=1070,
           linewidth=2.0,
           color="pink",
           label='Mode of DEP_DELAY = {}'.format(sample_data.DEP_DELAY.mode()[0]));
plt.vlines(sample_data.DEP_DELAY.std(),
           ymin=-90, 
           ymax=1070,
           linewidth=2.0,
           color="lightgreen",
           label='Standard Deviation of DEP_DELAY = {:+.2f}'.format(sample_data.DEP_DELAY.std()));

plt.hlines(sample_data.ARR_DELAY.mean(),
           xmin=-90, 
           xmax=1070,
           linewidth=2.0,
           color="purple",
           label='Mean of ARR_DELAY = {:+.2f}'.format(sample_data.ARR_DELAY.mean()));
plt.hlines(sample_data.ARR_DELAY.median(),
           xmin=-90, 
           xmax=1070,
           linewidth=2.0,
           color="orange",
           label='Median of ARR_DELAY = {:+.2f}'.format(sample_data.ARR_DELAY.median()));
plt.hlines(sample_data.ARR_DELAY.mode()[0],
           xmin=-90, 
           xmax=1070,
           linewidth=2.0,
           color="cyan",
           label='Mode of ARR_DELAY = {}'.format(sample_data.ARR_DELAY.mode()[0]));
plt.hlines(sample_data.ARR_DELAY.std(),
           xmin=-90, 
           xmax=1070,
           linewidth=2.0,
           color="red",
           label='Standard Deviation of ARR_DELAY = {:+.2f}'.format(sample_data.ARR_DELAY.std()));


plt.plot(sample_data.DEP_DELAY,sample_data.ARR_DELAY,'g.')
plt.title("August 2018 Nationwide Airplane Delay Statistic")
plt.xlabel("Departure Delay (HHMM)")
plt.ylabel("Arrival Delay (HHMM)")

plt.legend(loc='lower right')
plt.show()


