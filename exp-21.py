import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv("rare_elements.csv")
values = data.iloc[:, 0].values

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g., 0.95): "))
precision = float(input("Enter desired precision: "))

sample = np.random.choice(values, n, replace=False)
mean = np.mean(sample)
std = np.std(sample, ddof=1)
alpha = 1 - confidence
z = stats.norm.ppf(1 - alpha/2)
margin = z * (std / np.sqrt(n))

lower = mean - margin
upper = mean + margin

print("Sample Mean:", mean)
print("Confidence Interval:", (lower, upper))
print("Precision Achieved:", margin)
