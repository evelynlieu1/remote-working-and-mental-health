import pandas as pd

# Load dataset
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

# 1. Missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())

# 3. Default/placeholder values
default_placeholders = ['NA', 'N/A', '-', 'None', 'null', 'NaN']
default_counts = (df.isin(default_placeholders).sum())
print("\nDefault/placeholder values per column:")
print(default_counts)

# 4. Incorrect values – check categorical unique values
categorical_cols = df.select_dtypes(include=['object']).columns
print("\nUnique values per categorical column:")
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

# 5. Inconsistent values – check numeric ranges
print("\nNumeric value ranges:")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    print(f"{col}: min={df[col].min()}, max={df[col].max()}")

