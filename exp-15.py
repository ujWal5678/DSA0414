import pandas as pd

# Load the social media dataset
df = pd.read_csv("socialmedia.csv")

# Display first few rows (optional)
df.head()

# Calculate frequency distribution of likes
likes_frequency = df['Likes'].value_counts().sort_index()

# Display the frequency distribution
print(likes_frequency)

likes_freq_df = likes_frequency.reset_index()
likes_freq_df.columns = ['Number_of_Likes', 'Frequency']

likes_freq_df
