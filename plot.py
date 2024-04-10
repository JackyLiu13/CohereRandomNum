import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import Counter
import json

# Define the dictionary
#read in hundred.json to numbers in dictionary
with open('numbers.json', 'r') as f:
    numbers = json.load(f)

# Initialize a dictionary to store the frequency of numbers
frequency = {}

# Calculate the frequency of numbers
for key, values in numbers.items():
    frequency[key] = dict(Counter(values))

# Convert the frequency dictionary to a DataFrame and transpose it
df = pd.DataFrame(frequency).T

# Reindex the DataFrame to include all numbers from 1 to 100
df = df.reindex(columns=range(1, 101), fill_value=0)

# Sort the columns
df = df.reindex(sorted(df.columns), axis=1)

# Reverse the order of the rows
df = df.iloc[::-1]

# Create a mask for values that are 0
mask = df == 0

# Create a custom colormap with Cohere colour scheme, green = cold, pink = medium, orange = hot
cmap = mcolors.LinearSegmentedColormap.from_list("custom", ["#517f6e","#d18ee2", "#ff7759"], N=256)

# Set the color of non-filled areas
plt.figure(figsize=(10, 8))
plt.gca().set_facecolor('#39594d')


# Plot the heatmap with the mask and capture the return value
ax = sns.heatmap(df, cmap=cmap, annot=True, fmt=".0f", mask=mask)


# Get columns that have at least one non-zero value
non_zero_columns = df.loc[:, (df != 0).any(axis=0)].columns

# Set the xticks to the non-zero columns and rotate the labels 90 degrees for visibility
ax.set_xticks(non_zero_columns)
ax.set_xticklabels(non_zero_columns, rotation=90)

# Set the label of the color bar
colorbar = ax.collections[0].colorbar
colorbar.set_label("Frequency")
        

plt.title("Distribution of Cohere picking a number between 0 - 100 for different temperatures")
plt.xlabel("Number Selected By Cohere")
plt.ylabel("Temperature")
plt.show()