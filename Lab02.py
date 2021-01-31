import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")
plt.plot(sample_data.DEP_DELAY,sample_data.ARR_DELAY)
plt.show
