import pandas as pd

# Load the dataset
df = pd.read_csv('data/winequality-red.csv')

# View the first few rows
print(df.head())

# Check basic info
# print(df.info())

# Summary statistics
# print(df.describe())

# Check for missing values
# print(df.isnull().sum())
