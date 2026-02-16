# Import required libraries
from collections import Counter
import string

# Step 1: Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Step 2: Convert text to lowercase
text = text.lower()

# Step 3: Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Step 4: Split text into words
words = text.split()

# Step 5: Calculate frequency distribution
word_frequency = Counter(words)

# Step 6: Display word frequencies
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
