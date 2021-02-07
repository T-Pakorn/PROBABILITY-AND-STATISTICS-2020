import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

x = sample_data.DEP_DELAY
y = sample_data.ARR_DELAY
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.boxplot(x)
ax1.set_title("Box Plot : Departure Delay")
ax1.set_ylabel("Departure Delay (HHMM)")
ax2.boxplot(y)
ax2.set_title("Box Plot : Arrival Delay")
ax2.set_ylabel("Arrival Delay (HHMM)")

plt.show()