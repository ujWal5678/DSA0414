import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
weather_data = pd.read_csv('temperature2.csv')

# Line plot for monthly temperature
plt.figure()
plt.plot(weather_data['date'], weather_data['meantemp'])
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Monthly Temperature Line Plot")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
weather_data = pd.read_csv('temperature2.csv')

# Scatter plot for monthly rainfall
plt.figure()
plt.scatter(weather_data['date'], weather_data['rainfall'])
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.title("Monthly Rainfall Scatter Plot")
plt.show()
