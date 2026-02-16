import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('bodyfat.csv')

print("The mean of Age is:", round(df['age'].mean(), 2))
print("The mean of Bodyfat is:", round(df['fat(%)'].mean(), 2))
print("The median Age is:", df['age'].median())
print("The median Bodyfat is:", df['fat(%)'].median())
print("The Standard Deviation Age is:", round(df['age'].std(), 2))
print("The Standard Deviation Bodyfat is:", round(df['fat(%)'].std(), 2))

plt.boxplot([df['age'], df['fat(%)']], labels=['Age', 'Body Fat %'])
plt.title("Distribution of Age and Body Fat")
plt.show()

plt.scatter(df['age'], df['fat(%)'],marker="o")
plt.title("Age vs Body Fat")
plt.xlabel("Age")
plt.ylabel("Body Fat %")
plt.show()
