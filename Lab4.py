import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math
import Converter

data = pd.read_csv("August_2018_Nationwide_Airplane_Delay_Statistic.csv")

x = data["ARR_DELAY"]
mean = Converter.convertToMin(str(x.mean()))
size = len(x)


intervals = []
sample_means = [mean,mean,mean]

z_critical_90 = stats.norm.ppf(q = 0.95) #90
z_critical_95 = stats.norm.ppf(q = 0.975) #95
z_critical_99 = stats.norm.ppf(q = 0.995) #99

pop_stdev = Converter.convertToMin(str(x.std()))

margin_of_error_90 = z_critical_90 * (pop_stdev/math.sqrt(size))
margin_of_error_95 = z_critical_95 * (pop_stdev/math.sqrt(size))
margin_of_error_99 = z_critical_99 * (pop_stdev/math.sqrt(size))

confidence_interval_90 = (mean - margin_of_error_90,
                       mean + margin_of_error_90)
intervals.append(confidence_interval_90)
confidence_interval_95 = (mean - margin_of_error_95,
                       mean + margin_of_error_95)
intervals.append(confidence_interval_95)
confidence_interval_99 = (mean - margin_of_error_99,
                       mean + margin_of_error_99)
intervals.append(confidence_interval_99)

print("90% z-critical value:")
print(z_critical_90)
print("ConfidenceLevel = 90% ---> Confidence interval:")
print(confidence_interval_90)
print()
print("95% z-critical value:")             
print(z_critical_95)  
print("ConfidenceLevel = 95% ---> Confidence interval:")
print(confidence_interval_95)
print()
print("99% z-critical value:")             
print(z_critical_99)  
print("ConfidenceLevel = 99% ---> Confidence interval:")
print(confidence_interval_99)

plt.figure(figsize=(9,9))
plt.errorbar(x=[90,95,99], 
             y=sample_means, 
             yerr=[(top-bot)/2 for top,bot in intervals],
             fmt='o',
             label=["ConfidenceLevel = 90%","ConfidenceLevel = 95%","ConfidenceLevel = 99%"])

plt.hlines(xmin=89, xmax=100,
           y=mean, 
           linewidth=2.0,
           color="red");

plt.title("Confidence Interval (CI) of Mean")
plt.xlabel("Confidence level in percentage (%)")
plt.ylabel("Arrival Delay in minute (Minutes)")
plt.show()




























