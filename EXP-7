import pandas as pd

# Load dataset
order_data = pd.read_csv('orders.csv')

# Correct column names from your dataset
customer_col = 'Customer ID'
date_col = 'Date Order was placed'
product_col = 'Product ID'
quantity_col = 'Quantity Ordered'

# Convert order date to datetime (safe parsing)
order_data[date_col] = pd.to_datetime(order_data[date_col], errors='coerce')

# 1. Total number of orders made by each customer
orders_per_customer = order_data.groupby(customer_col).size()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby(product_col)[quantity_col].mean()

# 3. Earliest and latest order dates
earliest_date = order_data[date_col].min()
latest_date = order_data[date_col].max()

# Display results
print("Total number of orders made by each customer:")
print(orders_per_customer)

print("\nAverage order quantity for each product:")
print(avg_quantity_per_product)

print("\nEarliest order date:", earliest_date)
print("Latest order date:", latest_date)
