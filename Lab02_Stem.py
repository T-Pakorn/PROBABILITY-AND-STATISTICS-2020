import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

x = sample_data.DEP_DELAY
y = sample_data.ARR_DELAY

import stemgraphic

fig, ax = stemgraphic.stem_graphic(x)
#fig, ax = stemgraphic.stem_graphic(y)

plt.show()