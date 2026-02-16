import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales1.csv')

monthly_sales = sales_data.groupby('Month_sales')['Total'].sum()

plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Line Plot")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales1.csv')

monthly_sales = sales_data.groupby('Month_sales')['Total'].sum()

plt.figure()
plt.scatter(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Scatter Plot")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales1.csv')

monthly_sales = sales_data.groupby('Month_sales')['Total'].sum()

plt.figure()
plt.bar(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Bar Plot")
plt.show()
