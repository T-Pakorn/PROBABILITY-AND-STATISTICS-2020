import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random
import math
import Converter
from sklearn import linear_model


matplotlib.style.use('ggplot')
data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

# Initialize model
regression_model = linear_model.LinearRegression()

# Train the model using the mtcars data
regression_model.fit(X=pd.DataFrame(data["DEP_DELAY"]),
                     y=data["ARR_DELAY"])

# Check trained model y-intercept
print("Intercept = " + str(regression_model.intercept_))

# Check trained model coefficients
print("Coef = " + str(regression_model.coef_))

print("R-squared = " + str(regression_model.score(X=pd.DataFrame(data["DEP_DELAY"]),
                       y=data["ARR_DELAY"])))

train_prediction = regression_model.predict(X = pd.DataFrame(data["DEP_DELAY"]))

# Actual - prediction = residuals
residuals = data["ARR_DELAY"] - train_prediction

print(residuals.describe())

SSResiduals = (residuals**2).sum()

SSTotal = ((data["ARR_DELAY"] - data["ARR_DELAY"].mean())**2).sum()

# R-squared
print("R-squared by hand = " + str(1 - (SSResiduals/SSTotal)))

data.plot(kind="scatter",
          x="DEP_DELAY",
          y="ARR_DELAY",
          figsize=(9, 9),
          color="black")

# Plot regression line
plt.plot(data["DEP_DELAY"],      # Explanitory variable
         train_prediction,  # Predicted values
         color="blue");
plt.title("Linear Regression")
plt.xlabel("Departure Delay Time (Minutes)")
plt.ylabel("Arrival Delay Time (Minutes)")
plt.show()
