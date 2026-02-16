import pandas as pd

# Load dataset
sales_data = pd.read_csv('sales1.csv')

# Correct columns from your dataset
product_col = 'Product_Name'
quantity_col = 'Quantity_Sold'

# Group by product and sum quantity sold
top_5_products = (
    sales_data
    .groupby(product_col)[quantity_col]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Display result
print("Top 5 products sold the most in the past month:")
print(top_5_products)
