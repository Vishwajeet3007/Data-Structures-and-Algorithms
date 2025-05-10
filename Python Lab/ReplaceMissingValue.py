""" 
Write a Pandas program to find and replace the missing values in a given DataFrame which do 
not have any valuable information. 
"""
import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [24, np.nan, 30, 29, np.nan],
    'City': ['New York', 'Los Angeles', np.nan, 'Chicago', 'Houston'],
    'Score': [85, np.nan, 75, 90, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Method to find and replace missing values
def replace_missing_values(df):
    # Replace missing values in 'Name' column with 'Unknown'
    df['Name'].fillna('Unknown', inplace=True)
    
    # Replace missing values in 'Age' column with the mean age
    mean_age = df['Age'].mean()
    df['Age'].fillna(mean_age, inplace=True)
    
    # Replace missing values in 'City' column with 'Unknown'
    df['City'].fillna('Unknown', inplace=True)
    
    # Replace missing values in 'Score' column with the mean score
    mean_score = df['Score'].mean()
    df['Score'].fillna(mean_score, inplace=True)
    
    return df

# Replace missing values in the DataFrame
df = replace_missing_values(df)
print("\nDataFrame after replacing missing values:")
print(df)
