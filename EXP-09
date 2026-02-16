import pandas as pd

# Load dataset
property_data = pd.read_csv('House_Prediction.csv')

# Show column names
print("Columns in dataset:")
print(property_data.columns)

# ---- Assign columns based on dataset order ----
property_id_col = property_data.columns[0]
location_col = property_data.columns[1]
bedrooms_col = property_data.columns[2]
area_col = property_data.columns[3]
price_col = property_data.columns[4]

# 1. Average listing price of properties in each location
avg_price_by_location = property_data.groupby(location_col)[price_col].mean()

# 2. Number of properties with more than four bedrooms
properties_more_than_4_bedrooms = property_data[property_data[bedrooms_col] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data[area_col].idxmax()]

# Display results
print("\nAverage listing price in each location:")
print(avg_price_by_location)

print("\nNumber of properties with more than four bedrooms:")
print(properties_more_than_4_bedrooms)

print("\nProperty with the largest area:")
print(largest_area_property)
