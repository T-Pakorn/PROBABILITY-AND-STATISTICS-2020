import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")
plt.plot(sample_data.DEP_DELAY,sample_data.ARR_DELAY,'g.')
plt.title("August 2018 Nationwide Airplane Delay Statistic")
plt.xlabel("Departure Delay (HHMM)")
plt.ylabel("Arrival Delay (HHMM)")
plt.show()
