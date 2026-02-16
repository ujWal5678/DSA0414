
import pandas as pd

# Load the sales data (example: CSV file)
df = pd.read_csv("onlinesales.csv")

# Display first few rows (optional)
df.head()

# Calculate frequency distribution of customer ages
age_frequency = df['Age'].value_counts().sort_index()

# Display the result
print(age_frequency)
