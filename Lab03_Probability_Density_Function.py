import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

x = sample_data["DEP_DELAY"]
y = sample_data["ARR_DELAY"]

DEP_DELAY_COUNT, DEP_DELAY_BIN = np.histogram(x,bins=10)
ARR_DELAY_COUNT, ARR_DELAY_BIN = np.histogram(y,bins=10)

DEP_DELAY_PDF = DEP_DELAY_COUNT / sum(DEP_DELAY_COUNT)
DEP_DELAY_CDF = np.cumsum(DEP_DELAY_PDF)
ARR_DELAY_PDF = ARR_DELAY_COUNT / sum(ARR_DELAY_COUNT)
ARR_DELAY_CDF = np.cumsum(ARR_DELAY_PDF)

figure, DEP_DELAY = plt.subplots(1,2,figsize=(18,9),sharey=True)
DEP_DELAY[0].set_title("Departure Delay Time (Probability Density Function (PDF))")
DEP_DELAY[0].set_xlabel("Departure Delay Time (Minutes)")
DEP_DELAY[0].set_ylabel("The Probability of the plane will gain departure delay")
DEP_DELAY[0].plot(DEP_DELAY_BIN[1:],DEP_DELAY_PDF,color="red")
DEP_DELAY[0].legend()

DEP_DELAY[1].set_title("Departure Delay Time (Cumulative Probability Function (CDF))")
DEP_DELAY[1].set_xlabel("Departure Delay Time (Minutes)")
DEP_DELAY[1].set_ylabel("The Probability of the plane will gain departure delay")
DEP_DELAY[1].plot(DEP_DELAY_BIN[1:],DEP_DELAY_CDF,color="red")
DEP_DELAY[1].legend()

figure, ARR_DELAY = plt.subplots(1,2,figsize=(18,9),sharey=True)
ARR_DELAY[0].set_title("Arrival Delay Time (Probability Density Function (PDF))")
ARR_DELAY[0].set_xlabel("Arrival Delay Time (Minutes)")
ARR_DELAY[0].set_ylabel("The Probability of the plane will gain arrival delay")
ARR_DELAY[0].plot(ARR_DELAY_BIN[1:],ARR_DELAY_PDF,color="red")
ARR_DELAY[0].legend()

ARR_DELAY[1].set_title("Arrival Delay Time (Cumulative Probability Function (CDF))")
ARR_DELAY[1].set_xlabel("Arrival Delay Time (Minutes)")
ARR_DELAY[1].set_ylabel("The Probability of the plane will gain arrival delay")
ARR_DELAY[1].plot(ARR_DELAY_BIN[1:],ARR_DELAY_CDF,color="red")
ARR_DELAY[1].legend()

plt.show()