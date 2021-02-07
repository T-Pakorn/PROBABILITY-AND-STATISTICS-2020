import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

x = sample_data.DEP_DELAY
y = sample_data.ARR_DELAY
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.hist(x)
ax1.set_title("Departure Delay Time to Number of Flights")
ax1.set_xlabel("Departure Delay (HHMM)")
ax2.hist(y)
ax2.set_title("Arrival Delay Time to Number of Flights")
ax2.set_xlabel("Arrival Delay (HHMM)")
ax1.set_ylabel("Number Of Flights (Flights)")


plt.show()